#!/usr/bin/env python

import mysql.connector

conn=mysql.connector.connect(user='jstern19',password='Password',host='localhost')
mycursor=conn.cursor(buffered=True)
mycursor.execute("CREATE DATABASE 601Project3")
