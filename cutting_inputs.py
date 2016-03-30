
		# HOW TO BREAK BY FULL STOPS

import csv


all_inputs = csv.reader(open("output"+".csv", 'r'), delimiter=',')
file_number = 0
path = "breaks/"
file_name_tag = "break_at_"
global_doc = {}

for x in xrange(1, 3):
	global_doc[x] = []

for row in all_inputs:
	sentiment = row[0]
	review = row[1]
	file_number = 0
	sentence = ""
	for char in review:
		if (char == "."):
			l = []
			l.append(sentiment)
			l.append(str(sentence))
			file_number += 1
			if(file_number > 2):
				continue
			global_doc[file_number].append(l)
		else:
			sentence += char

for key in global_doc:
 	with open(path + file_name_tag + str(key) + ".csv", "wb") as csv_writer:
 		writer = csv.writer(csv_writer)
 		writer.writerows(global_doc[key])