import csv

__author__ = 'charlie'

breakfast = raw_input("what do you want to eat for breakfast? ")

lunch = raw_input("what do you want to eat for lunch? ")

dinner = raw_input("what do you want to eat for dinner? ")

with open('meal.csv', 'wb') as csvFile:
    mealWriter = csv.writer(csvFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    mealWriter.writerow(['Breakfast'] + [breakfast])
    mealWriter.writerow(['Lunch'] + [lunch])
    mealWriter.writerow(['Dinner'] + [dinner])

with open('meal.csv', 'rb') as guy:
    mealReader = csv.reader(guy, delimiter=',', quotechar='|')
    for row in mealReader:
        print row[1]




