# EC601 Mini-Project 3: Databases
This project uses the twitter API to obtain photos from a twitter feed, convert them into a video slideshow, and download descriptions of each photo in a text file called image_descriptions.txt. In this branch, I have implemented mysql and mongodb databases that are used to store data about users and their respective sessions. 

## Setup 
The first modification that must be made to the following files is that you have to insert your twitter API account keys into passwords.py and your google API account keys into account_key.json.

To run:
1. insert twitter api keys in passwords.py
2. insert google api keys in account_key.json
3. open finalscript.sh and follow the instructions to change the arguments of the first python script call
4. run finalscript.sh
