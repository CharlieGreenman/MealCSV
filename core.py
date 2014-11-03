__author__ = 'charlie'
#import the csv engine
import csv
#give meal.csv the name f from nkw on
with open('meal.csv') as f:
    #assign f_csv variable as an iteration over the lines given in the csvfile
    f_csv = csv.reader(f)
    #assign a headers variable which calls the next line everytime it is called
    # unneccesary as of now headers = next(f_csv)
    for row in f_csv:
        print row[1]