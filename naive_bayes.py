import re
import csv
import datetime
import nltk


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



start_time = datetime.datetime.now()
start_minute = start_time.minute
start_second = start_time.second
start_microsecond = start_time.microsecond


end_time = datetime.datetime.now()
end_minute = end_time.minute
end_second = end_time.second
end_microsecond = end_time.microsecond

minutes_taken = end_minute - start_minute
seconds_taken = abs(end_second - start_second)
microseconds_taken = abs(end_microsecond - start_microsecond)


fp = csv.reader(open("output"+".csv", 'r'), delimiter=',')
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
#print NBC.classify(extract_features(getFeatureVector(processedReview)))



correct = 0
incorrect = 0
done = 1

for test in testing_set:
    result = NBC.classify(extract_features(test[0]))
    if (result == test[1]):
        correct = correct + 1
    else:
        incorrect = incorrect + 1
    print "testing %d"%done
    done = done + 1 

# correct = 0
# incorrect = 0
# done = 1

# fp = csv.reader(open("test_nbc_"+".csv"))
# for row in fp:
#     sentiment = row[0]
#     review = row[1]
#     processedReview = processReview(review)
#     result = NBC.classify(extract_features(getFeatureVector(processedReview)))
#     if(result == sentiment):
#         correct = correct + 1
#     else:
#         incorrect = incorrect + 1
#     print "testing %d"%done
#     done = done + 1


accuracy = 100.0*(float(correct)/(float(correct) + float(incorrect)))
print accuracy



end_time = datetime.datetime.now()
end_minute = end_time.minute
end_second = end_time.second
end_microsecond = end_time.microsecond

minutes_taken = end_minute - start_minute
seconds_taken = abs(end_second - start_second)
microseconds_taken = abs(end_microsecond - start_microsecond)
