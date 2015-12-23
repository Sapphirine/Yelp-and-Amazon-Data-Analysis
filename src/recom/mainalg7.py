import csv
import json
import operator
import sys

business_id_set = set()
user_id_set = set()
review_id_set=set()
user_review_rating_sum_dict = {}
user_review_count_dict = {}
Uiddictionary=dict()
Biddictionary=dict()


def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False
def review_converter():
	dataset = open('yelpreview.csv', 'r')
	writer = csv.writer(open('reviewconvert.csv', 'w'))
	UidCount=1
	BidCount=1

	for line in dataset.read().splitlines():
		array=line.split(',')
		size=len(array)

		Uid=array[1]
		Bid=array[2]
		Sta=int(array[3])

		if Uid not in user_id_set:
			user_id_set.add(Uid)
			Uiddictionary[Uid]=UidCount
			UidCount=UidCount+1
		
		if Bid not in Biddictionary:
			business_id_set.add(Bid)
			Biddictionary[Bid]=BidCount
			BidCount=BidCount+1
			
		
			#print BidCount
			#print Bid

		outputuid=Uiddictionary.get(Uid)
		outputbid=Biddictionary.get(Bid)

		writer.writerow([outputuid, outputbid, Sta])


	dataset.close()

def main():
	review_converter()

main()
