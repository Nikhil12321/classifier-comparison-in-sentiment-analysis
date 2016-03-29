import nltk
import os

file = open('data/pos/cv000_29590.txt', 'r')
inp = file.read()
l = []
l.append(-1)
l.append(inp)
print l


#
#	TOKENIZE AN INPUT
#
# tokens = nltk.word_tokenize(inp)
# print tokens