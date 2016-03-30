
		# HOW TO BREAK BY FULL STOPS

import csv


all_inputs = csv.reader(open("oo"+".csv", 'r'), delimiter=',')

something = ""

for row in all_inputs:
	review = row[1]
	for char in review:
		if (char != "."):
			something += char
		else:
			break
	print something
	something = ""


