# this program calculates the total number of times each word has been tweeted.
import sys

#get file path from command line argument in python
infile=open(sys.argv[1],"r+")

outfile=open(sys.argv[2],"w")

#dictionary containing key (tweeted word) and value (total number of times each tweeted word) 
word_count = {}

for line in infile:
    data = line.strip().split(" ")
    for key in data:
        if key in word_count.keys():
            word_count[key] +=1
        else:
            word_count[key] = 1

#find the longest string (key) in the dictionary word_count 
width = len(max(sorted(word_count),key=len)) + 4

for key in sorted(word_count):
   outfile.write(key.ljust(width))
   outfile.write(repr(word_count[key]))
   outfile.write("\n")

outfile.close()
