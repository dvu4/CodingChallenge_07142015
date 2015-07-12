# this program calculates the median number of unique words per tweet.
import numpy as np
import sys

#getting file path from command line argument in python
infile=open(sys.argv[1],"r+")
outfile=open(sys.argv[2],"w")

#the number of unique words in each tweet
num_word=0
#the set of unique words per tweet 
set_word=[]

for line in infile:
    line1 = [] 
    for w in list(set(line.split())): # set: remove duplicate elements in list
        line1.append(w)
    num_word = len(line1)
    set_word.append(num_word)
    print 'the number of unique words in each tweet is:',set_word,'\n'
    print 'median is:', np.median(set_word)
    outfile.write(format(np.median(set_word),'.2f'))
    #outfile.write(repr(np.median(set_word)))
    outfile.write("\n")
    
outfile.close()
