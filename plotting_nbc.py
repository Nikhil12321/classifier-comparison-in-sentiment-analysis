import pylab as pl
import numpy as np


#################################################################
####################### ACCURACY PRINT ##########################

# accuracies = open('nbc_stats_accuracy.txt', 'r')
# line_number = []
# accuracy = []
# for line in accuracies:
# 	a = line.split(' ')
# 	line_number.append(a[0])
# 	accuracy.append(a[1][:-1])

# pl.scatter(line_number, accuracy)
# pl.plot(line_number, accuracy)
# pl.show()

#################################################################
#################################################################

accuracies = open('nbc_stats_times', 'r')
line_number = []
accuracy = []
for line in accuracies:
	a = line.split(' ')
	line_number.append(a[0])
	accuracy.append(a[1][:-1])

pl.scatter(line_number, accuracy)
pl.plot(line_number, accuracy)
pl.show()

