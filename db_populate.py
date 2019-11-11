import csv
import sqlite3
import os


def insert(filepath):
    with open(filepath, "r") as input_csv:
        reader = csv.reader(input_csv)
        header = next(reader)
        
        
        
        for row in reader:
            host_id = row[2]
            host_name = row[3]
            number_of_reviews = row[11]
            neighborhood_group = row[4]
            neighborhood = row[5]
            latitude = row[6]
            longitude = row[7]
            price = row[9]

            add_host(host_id, host_name, number_of_reviews)
            add_house(neighborhood_group, neighborhood, latitude, longitude, price, host_id)


def add_host(host_id, host_name, number_of_reviews):
    with sqlite3.connect('airbnb.db') as conn:
        cursor = conn.cursor()
        
        SQL = """INSERT INTO host(host_id, host_name, number_of_reviews) VALUES (?,?,?);"""
        cursor.execute(SQL, (host_id, host_name, number_of_reviews))
        
 
def add_house(neighborhood_group, neighborhood, latitude, longitude, price, host_id):
    with sqlite3.connect('airbnb.db') as conn:
        cursor = conn.cursor()
        
        SQL = """INSERT INTO house(neighborhood_group, neighborhood, latitude, longitude, price, host_id) VALUES (?,?,?,?,?,?);"""
        cursor.execute(SQL, (neighborhood_group, neighborhood, latitude, longitude, price, host_id))       
       
       
if __name__ == "__main__":
    insert("ab_nyc_2019.csv")


        
