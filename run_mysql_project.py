#!/usr/bin/env python

import os
import sys
import mysql_test


x = input("Please enter username: ")
y = input("How many photos do you want to search for? ")

cmd = "./finalscript.sh " + y
os.system(cmd)

#read image_descriptions.txt and concatenate each word into one long string
all_words = open("image_descriptions.txt").read().splitlines()
descriptors = ""
for line in all_words:
    descriptors = descriptors + line + ", "
descriptors = descriptors[0:len(descriptors)-2]

#store in database

mysql_test.add_new_session(str(x), str(y), descriptors)

myresult = mysql_test.user_image_count()
print(myresult)

myresult = mysql_test.most_popular()
print(myresult)

myresult = mysql_test.search_keyword('thigh')
print(myresult)
