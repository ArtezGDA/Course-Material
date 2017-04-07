#!/usr/bin/env python

import json
import random

daysPerMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
pageNames = ["home", "home", "home", "home", "home", "home", "contact", "news", "products", "news", "products", "news", "products", "faq", "faq"]

allData = {}

years = []
for y in range(2016, 2018):
    year = {}
    months = []
    for m in range(1, 13):
        month = {}
        days = []
        for d in range(1, daysPerMonth[m - 1] + 1):
            day = {}
            data = {}
            data['lastPage'] = random.choice(pageNames)
            data['unique'] = random.randint(1,100)
            data['pageViews'] = random.randint(1,1000)
            day['day'] = d
            day['data'] = data
            days.append(day)
        month['month'] = m
        month['days'] = days
        months.append(month)
    year['year'] = y
    year['months'] = months
    years.append(year)
allData['years'] = years

jsonfile = 'nested_structure.json'

with open(jsonfile, 'w') as outputFile:
	json.dump(allData, outputFile, indent=2, sort_keys=True)
