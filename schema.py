import os
import sqlite3


def schema(dbpath):
    with sqlite3.connect(dbpath) as conn:
        cursor = conn.cursor()
        
    SQL = """DROP TABLE IF EXISTS host;"""
    cursor.execute(SQL)
    
    SQL = """CREATE TABLE host(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        host_id VARCHAR(50),
        host_name VARCHAR(200),
        number_of_reviews INTEGER(5)
    );"""
    cursor.execute(SQL)
    
    
    
    SQL = """DROP TABLE IF EXISTS house;"""
    cursor.execute(SQL)
    
    SQL = """CREATE TABLE house(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        neighborhood_group VARCHAR(100),
        neighborhood VARCHAR(100),
        latitude INTEGER(5),
        longitude INTEGER(5),
        price FLOAT(10),
        host_id INTEGER(50),
        FOREIGN KEY (host_id) REFERENCES host(host_id)
    );"""
    cursor.execute(SQL)
    
if __name__ == "__main__":
    schema("airbnb.db")
        
    
    
    
    