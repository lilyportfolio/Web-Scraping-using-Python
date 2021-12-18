"""
Created on Sun Nov 28 04:59:44 2021

@author: chiachih
"""

from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import setup_driver


def get_courses(skills_needed):
    base_url = "https://www.coursera.org/courses"

    found_all, foundU_all = search_skills(skills_needed)
    result(found_all, foundU_all)
    recommended_courses = list(result(found_all, foundU_all))
    return recommended_courses


def search_skills(skills_needed):
    found_all = []
    foundU_all = []
    for i in range(len(skills_needed)):
        per20Skills = "%20".join(skills_needed[i])
        courseraUrl = "https://www.coursera.org/search?query=" + per20Skills
        driver = setup_driver.chrome_driver()
        driver.get(courseraUrl)
        timeout = 20
    
        WebDriverWait(driver, timeout)

        html_soup = BeautifulSoup(driver.page_source, "html.parser")

        found_all += html_soup.find_all("h2", {'class': "cds-1 card-title css-iyr9nj cds-3"})
        foundU_all += html_soup.find_all("a", {'class': "result-title-link"})

    return found_all, foundU_all


def result(found_all, foundU_all):
    base_url = "https://www.coursera.org/courses"
    # Create dictionary for course name and url
    dict_course = dict()
    for i in range(len(found_all)):
        # for course urls
        toUrl = foundU_all[i].get('href')
        print(toUrl)
        courseraUrl = base_url + toUrl

        # store info in dictionary Course Name -> Course Url
        dict_course[found_all[i].text] = courseraUrl
    

    
    













