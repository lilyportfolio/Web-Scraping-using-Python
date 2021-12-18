#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Please install the following packages:
pip install bs4
pip install PySimpleGUI
pip install json
pip install selenium
pip install itertools
pip install slate3k
'''

"""
Created on Sun Nov 28 04:59:44 2021

@author: prajwalmr
"""

import PySimpleGUI as sg

import monster_selenium as monster
import indeed_selenium as indeed
import CMU_selenium
import coursera_selenium as coursera
import resume_parser
import jobSkillsOffline
import CMU_courses

# set theme for UI
sg.theme('Reddit')
font = ("Arial", 11)

# Option to search for offline skills if search taking too long
# offline_jobs = jobSkillsOffline.getAllOfflineJobs()
# supported_jobs = []
# for k,v in offline_jobs.items():
#    supported_jobs.append(k)

# set-up GUI
gui_layout = [
    [sg.Text(
        "This tool finds the skills you are yet to acquire and recommends courses to acquire them, to get the job you always wanted.")],
    [sg.Text("Let's get some basic details about your career goals")],
    [sg.Text()],
    [sg.Text("Upload your resume")], [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse()],
    [sg.Text('Select the job title from below supported jobs:')],
    [sg.Combo(supported_jobs, default_value='software engineer', key='combo')],
    [sg.Button('Search CMU Courses')], [sg.Button('Search Online Courses')]
]

layout = gui_layout

# Create the Window
window = sg.Window('TartanHired', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break

    if event == 'Search CMU Courses' or event == 'Search Online Courses':
        resume_path = values[0]
        if resume_path != "" and resume_path != None and ".pdf" in resume_path:
            current_skills = set(resume_parser.get_current_skills(resume_path))

            # get required skills from Indeed
            demanded_skills_indeed = indeed.job_search(values['combo'], 'USA')

            # get required skills from Monster
            # demanded_skills_monster = monster.job_search(values['combo'], 'USA')

            demanded_skills = demanded_skills_indeed
            required_skills = set(demanded_skills) - set(current_skills)

            req_skill_list = "".join(skill + " " for skill in required_skills)

            if event == 'Search CMU Courses':
                recommended_courses = CMU_courses.get_courses(list(required_skills))

            if event == 'Search Online Courses':
                recommended_courses = set(coursera.get_courses(list(required_skills)))

            layout = [
                [sg.Button('Close')],
                # [sg.Text('Recommended Courses for skills : ' + req_skill_list)],
                *[[sg.Text(course), ] for course in recommended_courses]

            ]

            window1 = sg.Window('TartanHired').Layout(layout)
            window.Close()
            window = window1

        else:
            sg.popup('Invalid file path for resume')

    if event == 'Close':
        gui_layout = [
            [sg.Text(
                "This tool finds the skills you are yet to acquire and recommends courses to acquire them, to get the job you always wanted.")],
            [sg.Text("Let's get some basic details about your career goals")],
            [sg.Text()],
            [sg.Text("Upload your resume")], [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse()],
            [sg.Text('Select the job title from below supported jobs:')],
            [sg.Combo(supported_jobs, default_value='software engineer', key='combo')],
            [sg.Button('Search CMU Courses')], [sg.Button('Search Online Courses')]
        ]

        layout = gui_layout
        window1 = sg.Window('TartanHired').Layout(layout)
        window.Close()
        window = window1

window.close()
