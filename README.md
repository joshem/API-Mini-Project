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

To initialize the database, run:
```
python create_sql_db.py
```

If you want to clear the database for any reason, run:
```
python mysql_test.py
```

### MongoDB installaion

```
sudo apt-get install mongodb

pip install pymongo
```

The mongodb datatbase will take care of initializing itself. To clear it, run:

```
python mongo_test.py
```

## To run program with mysql:
```
python run_mysql_project3.py
```
The program will ask you for your name and the number of images you want to retrieve from twitter. After this, the program will download the images, convert them into a video format with ffmpeg, and create a text file called 'image_descriptions.txt' containing descriptions of the photos using the Google Vision API. Data will be automatically stored in the mysql database. 

To make use of the database, I have created mysql_test.py which contains a set of functions that allow for easy user acccess to statistics about past sessions. 

