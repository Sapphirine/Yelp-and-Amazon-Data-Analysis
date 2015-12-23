import csv
import json

TYPE_STRING = 'type'
BUSINESS_ID = 'business_id'
USER_ID = 'user_id'
UNAME = 'name'
AVESTARS='average_stars'
FRIENDS='friends'
REVIEWCOUNT='review_count'

def user_extractor():
	dataset = open('yelp_academic_dataset_user.json', 'r')
	writer = csv.writer(open('yelpuser1.csv', 'w'))
	#writer.writerow(['UserID', 'Name', 'Review_Count', 'Average_Stars'])

	for line in dataset:
		line_dict = json.loads(line)
		uid = line_dict[USER_ID].encode('utf-8')
		name = line_dict[UNAME].encode('utf-8')
		Ave_stars = line_dict[AVESTARS]
		Review_count=line_dict[REVIEWCOUNT]
		writer.writerow([uid, name, Review_count, Ave_stars])

	dataset.close()

def main():

	user_extractor()

main()