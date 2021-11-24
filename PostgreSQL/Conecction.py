import psycopg2

conn = psycopg2.connect(host="localhost",
    database="MioF",
    user="postgres",
    password="postgres123", 
    port="5433")

