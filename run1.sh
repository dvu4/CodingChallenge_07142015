#!/usr/bin/env bash

# example of the run script for running the word count

# I'll execute my programs, with the input directory tweet_input and output the files in the directory tweet_output
python ./src/words_tweeted.py ./tweet_input/tweets_test.txt ./tweet_output/ft11.txt
python ./src/median_unique.py ./tweet_input/tweets_test.txt ./tweet_output/ft22.txt