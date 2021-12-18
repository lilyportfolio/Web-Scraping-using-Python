# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 11:31:47 2021

@author: Adithi Reddy
"""

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import re

import skills_generator
import setup_driver

def get_url(title,location,i):
    url = f'https://www.indeed.com/jobs?q={title}&l={location}&start='+str(i)
    return url

def find_keywords():
    return re.compile('qualifications|skills|requirements|you\shave', re.IGNORECASE)

def get_links_indeed(jobs):
    links = []
    for job in jobs:
        try: 
            links.append(job.get_attribute('href'))
        except:
            links.append(None)
    return links

def check_skills_indeed(next_siblings, skills):
    for n in next_siblings:
        if n.name == 'p' or n.name == 'br':
            for c in n.children:
                if c.name == 'b' and not re.search(r'skills|qualifications|requirements|you\shave', c.contents[0], re.I):
                    return skills
                elif c.name == 'b' and re.search(r'skills|qualifications|requirements|you\shave', c.contents[0], re.I):
                    continue
                else:
                    skills.append(c)
        elif n.name == 'ul':
            li_list = n.findChildren('li', recursive=False)
            for li in li_list:
                skills.append(li.text)
    return skills
        
def get_data(jobs, driver):
       
    links = get_links_indeed(jobs)
    total_list = []
    for link in links:
        if link is not None:
           driver.get(link)
           driver.implicitly_wait(10)
           soup = BeautifulSoup(driver.page_source,'html.parser') 
           try:
            body = soup.find(re.compile('strong|b'), text=find_keywords())
            if body is not None:
                next_siblings = body.parent.next_siblings
                skills_list = []
                skills_list = check_skills_indeed(next_siblings, skills_list)
                one_job_skills = skills_generator.generate_bag(skills_list)

                total_list.append(one_job_skills)
            
           except:
                continue
        else:
            continue
    top_10_skills = skills_generator.generate_top_skills(total_list)

    return top_10_skills

def job_search(title,location):
    
    top_10_skills = []
    
    driver = setup_driver.chrome_driver()
    
    #iterate over pages
    for i in range(1, 3):
        url = get_url(title, location,i)
        driver.get(url)
        driver.implicitly_wait(5)
        jobs = driver.find_elements(By.CLASS_NAME,'result')
        top_10_skills = get_data(jobs, driver)
    
    driver.quit()

    return top_10_skills

    
if __name__ == "__main__":
    title = input("Enter job title: ")
    location = input("Enter job location: ")
    job_search(title, location)
    
    