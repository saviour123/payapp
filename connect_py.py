import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="192.168.1.9", port="5432")

print "Opened database successfully"
