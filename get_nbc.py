import re
import csv
import datetime
import nltk

def nbc(test_file_name):
	def processReview(review):
	    review = review.lower()
	    review = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',review)
	    review = re.sub('@[^\s]+','AT_USER',review)
	    review = re.sub('[\s]+', ' ', review)
	    review = re.sub(r'#([^\s]+)', r'\1', review)
	    review = review.strip('\'"')
	    return review

	def replaceTwoOrMore(s):
	    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
	    return pattern.sub(r"\1\1", s)

	def getStopWordList():
	    fileName = "stopwords.txt"
	    stopWords = []

	    fp = open(fileName, 'r')
	    line = fp.readline()
	    while line:
	        word = line.strip()
	        stopWords.append(word)
	        line = fp.readline()
	    fp.close()
	    return stopWords


	def getFeatureVector(review):
	    featureVectorr = []
	    words = review.split()
	    stopWords = getStopWordList()
	    for w in words:
	        w = replaceTwoOrMore(w)
	        w = w.strip('\'"?,.')
	        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
	        if (w in stopWords or val is None):
	            continue
	        else:
	            featureVectorr.append(w.lower())
	    return featureVectorr



	def extract_features(review):
	    review_words = set(review)
	    features = {}
	    for word in featureList:
	        features['contains(%s)' % word] = (word in review_words)
	    return features


	###########################################
	start_time = datetime.datetime.now()
	start_minute = start_time.minute
	start_second = start_time.second
	start_microsecond = start_time.microsecond
	###########################################



	fp = csv.reader(open(test_file_name, 'r'), delimiter=',')
	reviews = []
	testing_set = []
	featureList = []
	count = 1

	for row in fp:
	    sentiment = row[0]
	    review = row[1]
	    processedReview = processReview(review)
	    featureVector = getFeatureVector(processedReview)
	    if(count >= 901 and count <= 1000):
	    	testing_set.append((featureVector, sentiment))
	    elif(count >= 1901 and count <= 2000):
	    	testing_set.append((featureVector, sentiment))
	    else:
		    featureList.extend(featureVector)
		    reviews.append((featureVector, sentiment))

	    print "training %d"%count
	    count = count + 1



	featureList = list(set(featureList))

	training_set = nltk.classify.util.apply_features(extract_features, reviews)

	NBC = nltk.NaiveBayesClassifier.train(training_set)

	correct = 0
	incorrect = 0
	total_positive = 100.0
	total_negative = 100.0
	identified_pos = 0.0
	identified_neg = 0.0
	identified_correctly_positive = 0.0
	identified_correctly_negative = 0.0

	done = 1

	for test in testing_set:
		result = NBC.classify(extract_features(test[0]))

		if(result == '1'):
			identified_pos = identified_pos + 1
		else:
			identified_neg = identified_neg + 1

		if (result == test[1]):
			if(result == '1'):
				identified_correctly_positive = identified_correctly_positive + 1
			else:
				identified_correctly_negative = identified_correctly_negative + 1
			correct = correct + 1
		else:
			incorrect = incorrect + 1
		print "testing %d"%done
		done = done + 1 


	accuracy = 100.0*(float(correct)/(float(correct) + float(incorrect)))
	recall_pos = 100.0*(identified_correctly_positive/total_positive)
	recall_neg = 100.0*(identified_correctly_negative/total_negative)
	precision_pos = 100.0*(identified_correctly_positive/identified_pos)
	precision_neg = 100.0*(identified_correctly_negative/identified_neg)
	precision = (precision_pos + precision_neg)/2.0
	recall = (recall_pos + recall_neg)/2.0

	######################################################################
	end_time = datetime.datetime.now()
	end_minute = end_time.minute
	end_second = end_time.second
	minutes_taken = end_minute - start_minute
	seconds_taken = abs(end_second - start_second)
	seconds_taken_abs = float(seconds_taken)/60.0
	minutes_taken_abs = float(minutes_taken) + seconds_taken_abs
	#######################################################################

	return accuracy, precision, recall, minutes_taken_abs