from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.collocations import ngrams
from nltk.util import bigrams
import collections
from collections import Counter
import nltk
from operator import itemgetter

# Opening the input text file with read mode.
f = open("task4.txt", "r")

# Reading the text file
contentsoffile = f.read()

# Printing the contents of the file
print("Contents of the file:","\n", contentsoffile)
print("----------------------------------------------------")
print("-----------------------------------------------------")

# Performing word lemmatization
lem = WordNetLemmatizer()

# Tokenizing the contents of the file.
words = word_tokenize(contentsoffile)

print("Lemmatization with verb form of the words:")
for word in words:
  print(lem.lemmatize(word, pos='v'))

print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("Performing bi-gram on the text:")
cp = word_tokenize(contentsoffile)
li = []

# Accessing ngram function to find bigrams from the given text.
bigramfinder = ngrams(cp, 2)
for a in bigramfinder:
    li.append(a)
print(li)

print("-----------------------------------------------------")
print("-----------------------------------------------------")

# Using counter function to cpunt the number of occurances of each bigram.
word_count = Counter(li)
print(" Calculating the word frequency of Bi-Gram:")
print(word_count)

print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("Finding the top 5 bigrams:")
freqcnt = nltk.FreqDist(li)
tf = freqcnt.most_common(5)

# Printing top five bigrams  which are found out using most_common function.
print(tf)

with open('task4.txt' , 'r') as file:
    ln = file.readlines()
fit= ''

for mp in ln:
    fit= fit + mp
senti = sent_tokenize(fit)
rep_sent1 = []


for sentences in senti:
    for word,words in li:
        for ((cp, mp), l) in tf:
            if (word, words == cp, mp):
                rep_sent1.append(sentences)


# Printing the lines of text that contain the most common top five bigrams.
print("-----------------------------------------------------")
print("-----------------------------------------------------")
print ("\n Summarising the text and finding out the lines with top five bigrams")
fc = nltk.FreqDist(rep_sent1)
fff = fc.most_common(5)
for ke,val in fff:
    print("\n",ke)

