# Comparison of SVM, Naive Bayes and Maximum Entropy Classifiers in sentiment analysis
We compared accuracy, precision, recall and time to classify for all these classifiers for **different lenghts of texts**.
We refer different lengths as different number of sentences. This helps us see which classifiers work best for classifying short lengths of text such as tweets and which one work for long texts like movie reviews.

## What data did we take?
We took the data of movie reviews. Cut each review at each full stop and prepared different csv files for each length which are stored in the folder breaks. The script used to cut is in **cutting_inputs.py**

## Where is the data stored?
The data is stored in different files which can be distinguished by their names like:
'maxE_stats_accuracy.txt': stores accuracy of maximum entropy 
'nbc_stats_recall': stores recall of naive bayes
***However** all svm data is stored in svm_stats

## How to use it?
The files:
1. getMaxEntropy.py
2. get_nbc.py
3. getsvm.py

are called to return the accuracy, precision and recall of each classifier.
The main programs that call the above three are 
1. svm_output.py
2. nbc_output.py
3. output_maxEnt.py

## Where is the data
The data can be found in output.csv 
