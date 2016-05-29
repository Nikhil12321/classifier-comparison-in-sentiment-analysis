import csv


def get_max_full_stops():

	all_inputs = csv.reader(open("output"+".csv", 'r'), delimiter=',')
	max_full_stops = 0
	file_number = 0
	for row in all_inputs:
		review = row[1]
		full_stops = 0

		for char in review:
			if(char == "."):
				full_stops += 1
			if(full_stops > max_full_stops):
				max_full_stops = full_stops
				file_number = row
	return max_full_stops, row

number, row = get_max_full_stops()
print row[1]

count = 0
for char in row[0]:
	if(char == "and"):
		print count+1
	count = count + 1