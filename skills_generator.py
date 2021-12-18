# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21:31:40 2021

@author: xueyang2
"""

import itertools
from collections import Counter
import re
import skills_parser

def generate_bag(skills_list):
    split_words = str(skills_list).split()
    naked_words = [re.sub('[^a-zA-Z0-9]+', '', x) for x in split_words]
    combo_words = [naked_words[i] + ' ' + naked_words[i + 1] for i in range(len(naked_words) - 1)]

    bag_skills = naked_words + combo_words

    return bag_skills


def generate_top_skills(total_list):
    flatten_list = list(itertools.chain(*total_list))
    for i in range(len(flatten_list)):
        flatten_list[i] = flatten_list[i].lower()
    discard = skills_parser.getDiscard()
    d_list = [word for word in flatten_list if word not in discard]
    most_common_skills = [word for word, word_count in Counter(d_list).most_common(10)]

    return most_common_skills