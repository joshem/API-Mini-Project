# EC601 Mini-Project 3: Databases
This project uses the twitter API to obtain photos from a twitter feed, convert them into a video slideshow, and download descriptions of each photo in a text file called image_descriptions.txt. In this branch, I have implemented mysql and mongodb databases that are used to store data about users and their respective sessions. 

## Setup 
The first modification that must be made to the following files is that you have to insert your twitter API account keys into passwords.py and your google API account keys into account_key.json.

### MYSQL installation
```
sudo apt-get --purge remove mysql-server mysql-common mysql-client

sudo apt-get install mysql-server mysql-common mysql-client

pip install mysql-connector-python
```
Once you have installed the proper mysql packages, you can either use the database at the root user or create another user profile for yourself to use. To do so, active mysql by running:
```
sudo mysql

GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' IDENTIFIED BY 'password';
```

I used the username 'jstern19' and the password 'Password'. You can change this, but doing so would require modifications to the code files. So it would be easier for you to just keep this username and password.

### MongoDB installaion



To run:
1. insert twitter api keys in passwords.py
2. insert google api keys in account_key.json
3. open finalscript.sh and follow the instructions to change the arguments of the first python script call
4. run finalscript.sh
