#!/usr/bin/python


"""This script can be used to analyze data in the 2012 Presidential Campaign,
available from ftp://ftp.fec.gov/FEC/2012/pas212.zip - data dictionary is at
http://www.fec.gov/finance/disclosure/metadata/DataDictionaryContributionstoCandidates.shtml
"""

import csv
import fileinput

total = 0.0
candidList = []
minusAverage = 0.0

for row in csv.reader(fileinput.input(files=('itpas2.txt')), delimiter='|'):
    
    if fileinput.isfirstline():
        minimum = float(row[14])
        maximum = float(row[14])
        total = float(row[14])
        linesread = 1
        candidList.append(str(row[16]))

    if not fileinput.isfirstline():
        total += float(row[14])
        mintest = float(row[14])
        maxtest = float(row[14])
        if mintest < minimum and mintest > 0:
            minimum = mintest

        if maxtest > maximum and maxtest > 0:
            maximum = maxtest

        linesread += 1

        if str(row[16]) not in candidList:
            candidList.append(str(row[16]))
        

totalLinesRead = linesread
average = total / totalLinesRead

for row in csv.reader(fileinput.input(files=('itpas2.txt')), delimiter='|'):
    if fileinput.isfirstline():
        linesread = 1

    if not fileinput.isfirstline():
        linesread += 1

    if linesread == totalLinesRead / 2 or linesread == (totalLinesRead / 2) - .5:
        median = float(row[14])

for row in csv.reader(fileinput.input(files=('itpas2.txt')), delimiter='|'):
	
	minusAverage = (minusAverage) + ((float(row[14]) - average)**2)

standardDev = ((1/float(totalLinesRead)*minusAverage)**.5)
	
print "Total Lines Read: %s" % totalLinesRead
##### Print out the stats
print "Total Donations: %s" % total
print "Minimum: %s" % minimum
print "Maximum: %s" % maximum
print "Mean: %s" % average
print "Median: %s" % median
# square root can be calculated with N**0.5
print "Standard Deviation: %s" % standardDev

##### Comma separated list of unique candidate ID numbers
print "Candidates: ", candidList

def minmax_normalize(value):
    """Takes a donation amount and returns a normalized value between 0-1. The
    normilzation should use the min and max amounts from the full dataset"""
    ###
    # TODO: replace line below with the actual calculations
    for row in csv.reader(fileinput.input(files=('itpas2.txt')), delimiter='|'):
		norm = (float(row[14]) - minimum) / (maximum - minimum) 
    ###/

    return norm

##### Normalize some sample values
print "Min-max normalized values: %r" % map(minmax_normalize, [2500, 50, 250, 35, 8, 100, 19])


###Extra Credit: 

candidTotal = 0.0
candidMin = 0.0
candidMax = 0.0
#for i in candidList:
candidate = candidList[1]
for row in csv.reader(fileinput.input(files=('itpas2.txt')), delimiter='|'):
	if candidate == str(row[16]):
		
		candidTotal += float(row[14])	
		
		if candidMin == 0.0 and candidMax == 0.0:
			candidMin = float(row[14])
			candidMax = float(row[14])
		
		if float(row[14]) < candidMin and float(row[14]) > 0:
			candidMin = float(row[14])
		
		if float(row[14]) > candidMax and float(row[14]) > 0:
			candidMax = float(row[14])
			
print("Candidate "+str(1))
print("Total: "+str(candidTotal))
print("Minimum: "+str(candidMin))
print("Maximum: "+str(candidMax))
			


