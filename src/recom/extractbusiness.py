
import csv
import json

TYPE_STRING = 'type'
BUSINESS_ID = 'business_id'
USER_ID = 'user_id'
BNAME = 'name'
UNAME = 'name'
BSTATE = 'state'
BCITY = 'city'
STARS = 'stars'
REVIEW_COUNT = 'review_count'
REVIEW_TEXT = 'text'
CURRENT_STATE = 'AZ'
CATEGORIES='categories'


def business_extractor():
	dataset = open('yelp_academic_dataset_business.json', 'r')
	writer = csv.writer(open('yelpbusinesses.csv', 'w'))

	for line in dataset:

		line_dict = json.loads(line)
		bstate = line_dict[BSTATE].encode('utf-8')
		
		words=[];
		words=line_dict[CATEGORIES]
		str1=';'.join(words)
		bcategories=str1.encode('utf-8')
		bid = line_dict[BUSINESS_ID].encode('utf-8')
		bcity = line_dict[BCITY].encode('utf-8')
		stars = line_dict[STARS]
		review_count = line_dict[REVIEW_COUNT]
		writer.writerow([bid, bcity, bstate, stars, review_count, bcategories])

	dataset.close()

def main():

	business_extractor()

main()