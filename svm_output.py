from getsvm import svm


output = open('svm_stats.txt', 'w')
index = 1
end_at = 10
for x in range(index, end_at+1):
	f = "breaks/break_at_"
	accuracy = svm(f + str(x) + ".csv")
	output.write(x + " " + accuracy)
	output.write('\n')
print "Done!!!"
output.close()