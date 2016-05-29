from get_nbc import nbc
import time


output_acc = open('nbc_stats_accuracy.txt', 'a')
output_prec = open('nbc_stats_precision', 'a')
output_recall = open('nbc_stats_recall', 'a')
output_times = open('nbc_stats_times', 'a')

index = 10
end_at = 100
for x in range(index, end_at+1):
	f = "breaks/break_at_"
	accuracy, precision, recall, times = nbc(f + str(x) + ".csv")
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