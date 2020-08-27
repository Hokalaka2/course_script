#!/bin/python3

import sys
from sys import argv
import requests
from bs4 import BeautifulSoup
from array import *


def check_avail(tables):
    if tables[5].string == 0:
        pass


def search_class(search_term, table_row_col):
    result = []
    for row in table_row_col:
        if any(search_term in c for c in row):
            result.append(row)
    return result


def printing_classes(table_row_col):
    for r in table_row_col:
        for c in r:
            print(c, end='\n')
        print()


URL = "https://ssb-prod.ec.middlebury.edu/PNTR/saturn_midd.course_catalog_utlq.catalog_page_by_dept"
full_parameter_list = {

}
count = 1
for x in argv[1:]:
    if x.startswith('-'):
        count += 1
        full_parameter_list[x] = argv[count]
        continue
    count += 1

print(full_parameter_list)

website = requests.get(URL + "?p_term=202090&p_course_subj_code=" + full_parameter_list["-d"])
soup = BeautifulSoup(website.content, 'html.parser')
table_row = soup.find('tr').find_next('tr').find_all_next('tr')
table_row_col = [[]]
index = 0

for t in table_row:
    table_row_col.insert(index, list(t.stripped_strings))
    index += 1

search_term = ""

try:
    search_term = full_parameter_list["-s"]
    printing_classes(search_class(search_term, table_row_col))
except:
    printing_classes(table_row_col)
