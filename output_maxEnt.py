from getMaxEntropy import maxE
import time


output_acc = open('maxE_stats_accuracy.txt', 'a')
output_prec = open('maxE_stats_precision.txt', 'a')
output_recall = open('maxE_stats_recall.txt', 'a')
output_times = open('maxE_stats_times.txt', 'a')

index = 2
end_at = 30
for x in range(index, end_at+1):
	f = "breaks/break_at_"
	accuracy, precision, recall, times = maxE(f + str(x) + ".csv")
	print "accuracy %f\n"%accuracy
	print "precision %f\n"%precision
	print "recall %f\n"%recall
	print "time %f\n"%times
	output_acc.write(str(x) + " " + str(accuracy))
	output_acc.write('\n')
	output_prec.write(str(x) + " " + str(precision))
	output_prec.write('\n')
	output_recall.write(str(x) + " " + str(recall))
	output_recall.write('\n')
	output_times.write(str(x) + " " + str(times))
	output_times.write('\n')
	print "%d done "%x
	time.sleep(3)
print "Done!!!"
output_acc.close()
output_prec.close()
output_recall.close()
output_times.close()
