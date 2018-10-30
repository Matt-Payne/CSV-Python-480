tempStringAge = ''
import csv
totalHousesCounted = 0

totalPeopleInHouse = 0
f = open('2010_Census_Populations_by_Zip_Code.csv')
reader = csv.DictReader(f)
for row in reader:
    tempStringAge = row["Median Age"]
    if (float(tempStringAge) < 30):
        temp = row["Average Household Size"]
        totalPeopleInHouse = totalPeopleInHouse + float(temp)

        totalHousesCounted = totalHousesCounted + 1
        print(totalPeopleInHouse)
        print(totalHousesCounted)

final = float(totalPeopleInHouse)/float(totalHousesCounted)
print('number of people per Household under the age of 30 in LA ' + str(final))
