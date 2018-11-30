#!/usr/bin/env python

import os
import sys
import mongo_test


x = input("Please enter username: ")
y = input("How many photos do you want to search for? ")

#call finalscript.sh which runs API-Mini-project1 by downloading twitter photos, creating the video, and calling the Google Vision API.
cmd = "./finalscript.sh " + y
os.system(cmd)

#read image_descriptions.txt and concatenate each word into one long string
all_words = open("image_descriptions.txt").read().splitlines()
descriptors = ""
for line in all_words:
    descriptors = descriptors + line + ", "
descriptors = descriptors[0:len(descriptors)-2]

#store in database

mongo_test.add_new_session(str(x), str(y), descriptors)


#examples of how to use functions in mongo_test.py
myresult = mongo_test.user_image_count()
print(myresult)

myresult = mongo_test.most_popular()
print(myresult)

myresult = mongo_test.search_keyword('thigh')
print(myresult)
