import csv
import json
import operator
import sys

business_id_set = set()
user_id_set = set()
review_id_set=set()
user_review_rating_sum_dict = {}
user_review_count_dict = {}
dictionary=dict()
number=dict()

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False


def business_filter():
	dataset = open('yelpbusinesses.csv', 'r')
	writer = csv.writer(open('businesscountfilter.csv', 'w'))

	for line in dataset.read().splitlines():
		array=line.split(',')
		size=len(array)

		if not is_number(array[3]):
			continue
		if not is_number(array[4]):
			continue

		Bid=array[0]
		Bcity=array[1]
		Bstate=array[2]
		Bstars=float(array[3])
		Breviewcount=int(array[4])
		Bcategories=array[5]

		if Breviewcount<20:
			continue

		business_id_set.add(Bid)
		writer.writerow([Bid, Bcity, Bstate, Bstars, Breviewcount, Bcategories])

	dataset.close()

def review_filter():
	dataset = open('yelpreview.csv', 'r')
	writer = csv.writer(open('alg2reviewfilter.csv', 'w'))

	for line in dataset.read().splitlines():
		array=line.split(',')
		size=len(array)

		Rid=array[0]
		Uid=array[1]
		Bid=array[2]
		Sta=int(array[3])

		if Bid in business_id_set:
			user_id_set.add(Uid)
			writer.writerow([Rid, Uid, Bid, Sta])

	dataset.close()

def basic_recommendation():
	useridinput=raw_input('please input your userid: ')
	dataset = open('alg2reviewfilter.csv', 'r')
	datasetfilter=open('alg2reviewfilter.csv', 'r')
	datasetfilter2=open('alg2reviewfilter.csv', 'r')
	client_set=set()
	business_set_filter=set()


	for line in dataset.read().splitlines():
		array=line.split(',')
		size=len(array)

		Rid=array[0]
		Uid=array[1]
		Bid=array[2]
		Sta=int(array[3])

		if cmp(Uid, useridinput)==0:
			if Bid in business_id_set:
				for line in datasetfilter.read().splitlines():
					array2=line.split(',')
					size2=len(array)

					Rid2=array2[0]
					Uid2=array2[1]
					Bid2=array2[2]
					Sta2=int(array2[3])

					if cmp(Bid2, Bid)==0:
						if cmp(Uid, Uid2)!=0:
							client_set.add(Uid2)
							for line in datasetfilter2.read().splitlines():
								array3=line.split(',')
								size3=len(array)

								Rid3=array3[0]
								Uid3=array3[1]
								Bid3=array3[2]
								Sta3=int(array3[3])
								if cmp(Uid2, Uid3)==0:
										print Bid3
										business_set_filter.add(Bid3)


		else:
			continue
	#print business_set_filter
	dataset.close()
	datasetfilter.close()
	datasetfilter2.close()


def main():

	business_filter()
	review_filter()
	basic_recommendation()

main()
