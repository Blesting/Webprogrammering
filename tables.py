# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:01:08 2019

@author: Nestea
"""

def clear_tables(c):
    try:
        c.execute(''' 
                               DROP TABLE users;
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)
    try:
        c.execute(''' 
                               DROP TABLE tracks;
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)
    try:
        c.execute(''' 
                               DROP TABLE trackvars;
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)
    try:
        c.execute(''' 
                               CREATE TABLE users(
                               Id INTEGER PRIMARY KEY AUTOINCREMENT,
                               name TEXT,
                               age INTEGER,
                               gender INTEGER,
                               password TEXT,
                               email TEXT
                               );
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)
    try:
        c.execute(''' 
                               CREATE TABLE tracks(
                               Id INTEGER PRIMARY KEY AUTOINCREMENT,
                               user_id INTEGER,
                               name TEXT,
                               unit TEXT,
                               type INTEGER,
                               createdate TEXT,
                               scalesize INT
                               );
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)
    try:
        c.execute(''' 
                               CREATE TABLE trackvars(
                               Id INTEGER PRIMARY KEY AUTOINCREMENT,
                               track_id INTEGER,
                               starttime TEXT,
                               postdate TEXT,
                               value INT
                               );
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)


def create_tables(c):
    try:
        c.execute(''' 
                               CREATE TABLE users(
                               Id INTEGER PRIMARY KEY AUTOINCREMENT,
                               name TEXT,
                               age INTEGER,
                               gender INTEGER,
                               password TEXT,
                               email TEXT
                               );
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)
    try:
        c.execute(''' 
                               CREATE TABLE tracks(
                               Id INTEGER PRIMARY KEY AUTOINCREMENT,
                               user_id INTEGER,
                               name TEXT,
                               unit TEXT,
                               type INTEGER,
                               createdate TEXT,
                               scalesize INT
                               );
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)
    try:
        c.execute(''' 
                               CREATE TABLE trackvars(
                               Id INTEGER PRIMARY KEY AUTOINCREMENT,
                               track_id INTEGER,
                               starttime TEXT,
                               postdate TEXT,
                               value INT
                               );
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)


def clear_users(c):
    try:
        c.execute(''' 
                               DROP TABLE users;
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)

    try:
        c.execute(''' 
                               CREATE TABLE users(
                               Id INTEGER PRIMARY KEY AUTOINCREMENT,
                               name TEXT,
                               age INTEGER,
                               gender INTEGER,
                               password TEXT,
                               email TEXT
                               );
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)



def clear_tracks(c):
    try:
        c.execute(''' 
                               DROP TABLE tracks;
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)
    try:
        c.execute(''' 
                               DROP TABLE trackvars;
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)
    try:
        c.execute(''' 
                               CREATE TABLE tracks(
                               Id INTEGER PRIMARY KEY AUTOINCREMENT,
                               user_id INTEGER,
                               name TEXT,
                               unit TEXT,
                               type INTEGER,
                               createdate TEXT,
                               scalesize INT
                               );
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)
    try:
        c.execute(''' 
                               CREATE TABLE trackvars(
                               Id INTEGER PRIMARY KEY AUTOINCREMENT,
                               track_id INTEGER,
                               starttime TEXT,
                               postdate TEXT,
                               value INT
                               );
                               ''')
        print("---------------------------------------------------SUCCESS---------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------ERROR---------------------------------------------------")
        print(e)


