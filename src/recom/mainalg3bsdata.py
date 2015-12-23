import csv
import json
import operator
import sys
import os


def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

def extract_business2():
	dataset = open('yelpbusinesses.csv', 'r')
	writer = csv.writer(open('alg3businessdata.csv', 'w'))

	for line in dataset.read().splitlines():
		array=line.split(',')
		size=len(array)
		if not is_number(array[3]):
			continue
		Bid=array[0]
		Bcity=array[1]
		Bstate=array[2]
		Bstars=float(array[3])
		Breviewcount=array[4]
		Bcategories=array[5]

	
		writer.writerow([Bid, Bstars])

	dataset.close()

def main():
	extract_business2()

main()