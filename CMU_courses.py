#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 19:12:22 2021

@author: prajwalmr
"""
import json

# get unique courses from CMU from search

def get_courses(required_skills):
    with open('data/all_cmu_courses.json') as f:
        all_cmu_courses_data = json.load(f)

        unique_courses = {}

        recommended_courses = []

        for course, description in all_cmu_courses_data.items():
            for skill in required_skills:
                if (skill in course.lower()) or (skill in description['course_description'].lower()):
                    if description['course_no'] not in unique_courses:
                        recommended_courses.append({course: description['course_no']})
                        unique_courses[description['course_no']] = description['course_no']

    return recommended_courses
