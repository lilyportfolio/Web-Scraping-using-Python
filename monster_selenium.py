# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21:31:40 2021

@author: xueyang2
"""

import csv
import time
import re


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import setup_driver
import skills_generator

fieldnames = ['title', 'company','keywords']

'''
def setup_driver():
    driver_path = "./drivers/geckodriver"
    firefox_service = Service(driver_path)
    firefox_options = Options()

    firefox_options.headless = True
    driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
    return driver
'''


def get_url(title, location, i):
    template = 'https://www.monster.com/jobs/search?q={}&where={}&page={}'
    url = template.format(title, location, str(i))
    return url


def open_csv(fieldnames):
    with open('job.csv', mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        csv_file.close()


def find_keywords():
    return re.compile('skills', re.IGNORECASE) or re.compile('qualifications', re.IGNORECASE) or re.compile(
        'requirements', re.IGNORECASE) or re.compile('you have', re.IGNORECASE)


def check_skills(next_siblings, skills):
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


def write_csv(fieldnames, title_text, company_text, location_text, skills_list):
    with open('job.csv', mode='a') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'title': title_text, 'company': company_text,'keywords': skills_list})

def job_search(fieldnames):
    open_csv(fieldnames)
    user_title = input('Enter a job title: ')

    for i in range(1, 10):
        request_url = get_url(user_title, None, i)

        driver = setup_driver.firefox_driver()
        driver.get(request_url)
        time.sleep(2)

        print('Title: %s' % driver.title)
        print('url: %s' % driver.current_url)

        total_list = []

        for j in range(1, 10):

            try:
                wait = WebDriverWait(driver, 60)

                jobs = wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH,
                                                                                          '/html/body/div[1]/div[2]/main/div[2]/nav/section[1]/div[2]/div[1]/div/div/div/div/div[' + str(
                                                                                              j) + ']/article/div/a')))

                for job in jobs:
                    link = job.get_attribute('href')
                    driver.get(link)
                    print(driver.current_url)
                    time.sleep(20)

                    title = driver.find_element(By.TAG_NAME, 'h1')
                    print(title.text)
                    company = driver.find_element(By.TAG_NAME, 'h2')
                    print(company.text)
                    location = driver.find_element(By.TAG_NAME, 'h3')
                    print(location.text)

                    time.sleep(100)

                    soup = BeautifulSoup(driver.page_source, 'html.parser')

                    try:
                        body = soup.find(re.compile('strong|b'), text=find_keywords())
                        next_siblings = body.parent.next_siblings

                        skills_list = []
                        skills_list = check_skills(next_siblings, skills_list)

                        write_csv(fieldnames, title.text, company.text, location.text, skills_list)

                        one_job_skills = skills_generator.generate_bag(skills_list)
                        print(one_job_skills)

                        total_list.append(one_job_skills)
                        print(total_list)

                        driver.back()

                    except AttributeError:
                        driver.back()

            except Exception as e:
                driver.back()

        driver.quit()

    top_10_skills = skills_generator.generate_top_skills(total_list)
    print(top_10_skills)

if __name__ == "__main__":
    job_search(fieldnames)