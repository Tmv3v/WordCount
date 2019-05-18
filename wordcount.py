#!/usr/bin/env python3
import os
import re
import string
import csv
def wordcount(input, output):
    #wordcount
    wordlist = []
    for filename in os.listdir(input):
        if filename.endswith('.txt'):
            with open(os.path.join(input, filename), 'r') as txtf:
                text = [item.translate(str.maketrans('','',string.punctuation+string.digits)).strip().lower() for item in txtf.read().split()]
                wordlist += text
    wordlist = [x for x in sorted(wordlist) if x]
    wordfreq = []
    for w in wordlist:
        wordfreq.append(wordlist.count(w))
    worddict = dict(zip(wordlist, wordfreq))
    return worddict

inputPath = 'wc_input'
outputPath = 'wc_output'
worddict = wordcount(inputPath, outputPath)
f = open(os.path.join(outputPath, 'wc_result.txt'), 'w')
for k, v in worddict.items():
    f.write(str(k)+' '+str(v)+'\n')
    print(str(k)+' '+str(v))
