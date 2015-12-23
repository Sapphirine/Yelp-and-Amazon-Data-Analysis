
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

def user_extractor():
	dataset = open('yelpuser1.csv', 'r')
	writer = csv.writer(open('yelpgooduserfilter.csv', 'w'))
	writerbaduser = csv.writer(open('yelpbaduserfilter.csv', 'w'))
	writer.writerow(['UserID', 'Name', 'Review_Count', 'Average_Stars'])
	writerbaduser.writerow(['UserID', 'Name', 'Review_Count', 'Average_Stars'])

	for line in dataset.readlines():
		array=line.split(',')
		Uid=array[0]
		name=array[1]
		reviewcount=array[2]
		averagestars=array[3]
		if not is_number(reviewcount):
			continue

		if int(reviewcount)<6.0:
			if reviewcount not in user_id_set:
				user_id_set.add(Uid)
				writerbaduser.writerow([Uid, name, float(reviewcount), float(averagestars)])
			continue
		elif float(averagestars)==1.0:
			if reviewcount not in user_id_set:
				user_id_set.add(Uid)
				writerbaduser.writerow([Uid, name, float(reviewcount), float(averagestars)])
			continue
		elif float(averagestars)==5.0:
			if reviewcount not in user_id_set:
				user_id_set.add(Uid)
				writerbaduser.writerow([Uid, name, float(reviewcount), float(averagestars)])
			continue
		else:
			writer.writerow([Uid, name, float(reviewcount), float(averagestars)])

	dataset.close()

def review_extractor():
	dataset = open('yelpreview.csv', 'r')
	writer = csv.writer(open('yelpgoodreviewfilter.csv', 'w'))
	writerbadreview = csv.writer(open('yelpbadreviewfilter.csv', 'w'))

	writer.writerow(['Review_ID', 'User_ID', 'business_ID', 'Stars'])
	writerbadreview.writerow(['Review_ID', 'User_ID', 'business_ID', 'Stars'])

	for line in dataset.read().splitlines():
		array=line.split(',')
		size=len(array)

		Rid=array[0]
		Uid=array[1]
		Bid=array[2]
		Sta=int(array[3])
			
		if Uid in user_id_set:
			if Rid not in review_id_set:
				review_id_set.add(Bid)
				if Bid not in business_id_set:					
					business_id_set.add(Bid)
					number[Bid]=1
					dictionary[Bid]=Sta
				else:
					flag=dictionary.get(Bid)+Sta
					dictionary[Bid]=flag
					num=number.get(Bid)+1
					number[Bid]=num

				writerbadreview.writerow([Rid, Uid, Bid, Sta])
			continue
		else:
			writer.writerow([Rid, Uid, Bid, Sta])

	dataset.close()

def business_extractor():
	dataset = open('yelpbusinesses.csv', 'r')
	writer = csv.writer(open('yelpgoodbusinessfilter.csv', 'w'))
	writerbadreview = csv.writer(open('yelpbadbusinessfilter.csv', 'w'))

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

		totalstars=Bstars*Breviewcount

		if Breviewcount<5:
			continue

		if Bid in business_id_set:
			totalstars=float(totalstars-dictionary.get(Bid))
			newreviewcount=Breviewcount-number.get(Bid)
			if newreviewcount<5:
				continue

			newstars=float(totalstars/(newreviewcount))
			Bstars=newstars
			Breviewcount=newreviewcount

		writer.writerow([Bid, Bcity, Bstate, Bstars, Breviewcount, Bcategories])

	dataset.close()	

def filterplace():
	cityinput=raw_input('please input a city name: ')
	dataset = open('yelpgoodbusinessfilter.csv', 'r')
	writer = csv.writer(open('yelpbusinessfiltercity.csv', 'w'))

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

		if cmp(Bcity,cityinput)==0:
			writer.writerow([Bid, Bcity, Bstate, Bstars, Breviewcount, Bcategories])

	reader = csv.reader(open("yelpbusinessfiltercity.csv"), delimiter=",")
	csv_writer = csv.writer(open('finalresult.csv', 'w'))
	csv_writer.writerows(sorted(reader, key=operator.itemgetter(3), reverse=True))

	finalresult=open('finalresult.csv', 'r')
	countt=1

	for line in finalresult.read().splitlines():
		print line 
		if countt>5:
			break
		print countt
		countt = countt +1

	dataset.close()
	finalresult.close()

def main():

	user_extractor()
	review_extractor()
	business_extractor()
	filterplace()

main()