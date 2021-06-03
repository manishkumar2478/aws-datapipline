import psycopg2
import csv
conn = psycopg2.connect(
    host="127.0.0.1",
    database="BSENSE",
    user="postgres",
    password="Admin@123"
    )
curr = conn.cursor()
with open('C:\Stock_data\Company.csv','r') as f:
    curr.copy_from(f, 'bse.company', sep=',')
    print('Data loaded')
conn.commit()