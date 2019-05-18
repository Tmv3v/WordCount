#!/usr/bin/env python3
import os
import re
import string
import csv
import statistics
def runningMedian(input, output):
    #wordcount
    linelen = []
    runMedian = []
    for filename in sorted(os.listdir(input)):
        if filename.endswith('.txt'):
            with open(os.path.join(input, filename), 'r', encoding="utf-8") as txtf:
                for line in txtf:
                    words = line.translate(str.maketrans('','',string.punctuation+string.digits)).split()
                    if len(words)!=0:
                        linelen += [len(words)]
                        runMedian += ['{:g}'.format(statistics.median(linelen))]
    return runMedian

inputPath = 'wc_input'
outputPath = 'wc_output'
runMedian = runningMedian(inputPath, outputPath)
f = open(os.path.join(outputPath, 'med_result.txt'), 'w')
for i in runMedian:
    print(str(i))
    f.write(str(i)+'\n')
