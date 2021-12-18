#!/usr/bin/env python
# coding: utf-8

import setup_driver
import time

def get_recommended_courses(skills_needed):
    URL = "https://enr-apps.as.cmu.edu/open/SOC/SOCServlet/search"

    driver = setup_driver.chrome_driver()
    driver.get(URL)

    sem = driver.find_element_by_name("SEMESTER")
    sem.send_keys("Fall 2021")
    submit = driver.find_element_by_name("SUBMIT")
    submit.click()

    links = driver.find_elements_by_tag_name("a")

    course_object = {}

    for index in range(9, len(links)):

        links = driver.find_elements_by_tag_name("a")

        if (links[index].text != ""):
            try:
                links[index].click()
                time.sleep(2)

                modal_title = driver.find_elements_by_class_name("modal-title")

                for i in modal_title:
                    modal_data = i.text.split("\n")[1].split(" ")
                    course_no = modal_data[0]
                    course_title = ''.join(str(elem + " ") for elem in modal_data[2:])
                    cur_course_object = {}
                    cur_course_object['course_no'] = course_no

                # modal_content = driver.find_elements_by_id("course-detail-description")

                description = driver.find_elements_by_tag_name("p")

                for p in description:
                    if (len(p.text) > 0):
                        cur_course_object['course_description'] = p.text

                course_object[course_title] = cur_course_object

                close_button = driver.find_elements_by_tag_name("button")
                close_button[1].click()

            except Exception as e:
                print("error : " + str(e.args))

    recommended_courses = []

    for course, description in course_object.items():
        for skill in skills_needed:
            if (skill.strip() in course.lower()) or (skill.strip() in description['course_description'].lower()):
                recommended_courses.append({course: description['course_no']})
    return recommended_courses
