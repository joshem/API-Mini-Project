import mysql.connector
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
    conn=mysql.connector.connect(user='jstern19',password='Password',host='localhost',database='601Project3')
    mycursor=conn.cursor(buffered=True)
    try:
        mycursor.execute("CREATE TABLE users (username VARCHAR(255), tdate VARCHAR(255), numimages VARCHAR(255), descriptors VARCHAR(10000))")
    except:
        pass
    sql = "SELECT * FROM users"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    sql = "SELECT * FROM users"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    found_users = {}
    for x in myresult:
        if keyword in x[3]:
            if x[0] in found_users:
                found_users[x[0]].append(x[1])
            else:
                found_users[x[0]]=[]
                found_users[x[0]].append(x[1])
    return found_users

def most_popular():
    "Returns dictionary of descriptors and their respective popularities"
    conn=mysql.connector.connect(user='jstern19',password='Password',host='localhost',database='601Project3')
    mycursor=conn.cursor(buffered=True)
    try:
        mycursor.execute("CREATE TABLE users (username VARCHAR(255), tdate VARCHAR(255), numimages VARCHAR(255), descriptors VARCHAR(10000))")
    except:
        pass
    sql = "SELECT * FROM users"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    descriptors = {}
    for x in myresult:
        temp_descriptors = parse_descriptors(x[3])
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
    conn=mysql.connector.connect(user='jstern19',password='Password',host='localhost',database='601Project3')
    mycursor=conn.cursor(buffered=True)
    try:
        mycursor.execute("CREATE TABLE users (username VARCHAR(255), tdate VARCHAR(255), numimages VARCHAR(255), descriptors VARCHAR(10000))")
    except:
        pass
    sql = "SELECT * FROM users"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    user_counts = {}
    for x in myresult:
        if x[0] in user_counts:
            user_counts[x[0]] = str(int(user_counts[x[0]]) + int(x[2]))
        else:
            user_counts[x[0]] = x[2]
    return user_counts


def add_new_session(username, numimages, descriptors):
    "add new session statistics to database"
    conn=mysql.connector.connect(user='jstern19',password='Password',host='localhost',database='601Project3')
    mycursor=conn.cursor(buffered=True)
    try:
        mycursor.execute("CREATE TABLE users (username VARCHAR(255), tdate VARCHAR(255), numimages VARCHAR(255), descriptors VARCHAR(10000))")
    except:
        pass
    curr_time = datetime.datetime.now()
    mycursor.execute("""INSERT INTO users (username, tdate, numimages, descriptors) VALUES (%s, %s, %s, %s)""", (username, str(curr_time), numimages, descriptors))
    conn.commit()

if __name__ == '__main__':
    conn=mysql.connector.connect(user='jstern19',password='Password',host='localhost',database='601Project3')
    mycursor=conn.cursor(buffered=True)
    try:
        mycursor.execute("DROP TABLE users")
    except:
        pass
