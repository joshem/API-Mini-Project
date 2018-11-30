import pymongo
import datetime
import operator

def parse_descriptors(descriptors):
    new_descriptors = []
    temp_word = ""
    for i in descriptors:
        if(i != ",")and(i != " "):
            temp_word = temp_word + i
        else:
            if(temp_word != ""):
                new_descriptors.append(temp_word)
            temp_word = ""
    new_descriptors.append(temp_word)
    return new_descriptors

def search_keyword(keyword):
    "Returns list of users that found this keyword during their session and what time they found them"
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["601Project3"]
    mycol = mydb["users"]
    found_users = {}
    for x in mycol.find():
        if keyword in x['descriptors']:
            if x['username'] in found_users:
                found_users[x['username']].append(x['tdate'])
            else:
                found_users[x['username']]=[]
                found_users[x['username']].append(x['tdate'])
    return found_users

def most_popular():
    "Returns dictionary of descriptors and their respective popularities"
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["601Project3"]
    mycol = mydb["users"]
    descriptors = {}
    for x in mycol.find():
        temp_descriptors = parse_descriptors(x['descriptors'])
        for y in temp_descriptors:
            if y in descriptors:
                descriptors[y] = descriptors[y] + 1
            else:
                descriptors[y] = 1
    sorted_descriptors = sorted(descriptors.items(), key=operator.itemgetter(1))
    sorted_descriptors.reverse()
    return sorted_descriptors

def user_image_count():
    "Return number of images found by each user"
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["601Project3"]
    mycol = mydb["users"]
    user_counts = {}
    for x in mycol.find():
        if x['username'] in user_counts:
            user_counts[x['username']] = str(int(user_counts[x['username']]) + int(x['numimages']))
        else:
            user_counts[x['username']] = x['numimages']
    return user_counts


def add_new_session(username, numimages, descriptors):
    "add new session statistics to database"
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["601Project3"]
    mycol = mydb["users"]
    curr_time = datetime.datetime.now()
    mydict = { "username": username, "tdate": str(curr_time), "numimages": numimages, "descriptors": descriptors }
    x = mycol.insert_one(mydict)
    print(x.inserted_id)


if __name__ == '__main__':
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["601Project3"]
    mycol = mydb["users"]
    mycol.drop()
