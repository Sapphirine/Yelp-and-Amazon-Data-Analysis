import csv
import json


BUSINESS_ID = 'business_id'
USER_ID = 'user_id'
BCITY = 'city'
STARS = 'stars'
REVIEW_TEXT = 'text'
REVIEW_ID='review_id'


def review_extractor():
	dataset = open('yelp_academic_dataset_review.json', 'r')
	writer = csv.writer(open('yelpreview.csv', 'w'))
	#writer.writerow(['Review_ID', 'User_ID', 'business_ID', 'Stars'])

	for line in dataset:
		line_dict = json.loads(line)
		bid = line_dict[BUSINESS_ID].encode('utf-8')
		stars = line_dict[STARS]
		uid = line_dict[USER_ID].encode('utf-8')
		rid=line_dict[REVIEW_ID].encode('utf-8')
		rtext=line_dict[REVIEW_TEXT].encode('utf-8')

		writer.writerow([rid, uid, bid, stars])

	dataset.close()


def main():

	review_extractor()

main()