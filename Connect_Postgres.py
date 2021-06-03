import psycopg2
# connect to the PostgreSQL server
conn = psycopg2.connect(   
    host="127.0.0.1",
    database="BSENSE",
    user="postgres",
    password="Admin@123"
    )
		
# create a cursor
cur = conn.cursor()
        
# execute a statement
cur.execute('SELECT * FROM bse.Share_Detail')

# display the PostgreSQL database server version
tab_data = cur.fetchall()
print(tab_data)
       
	# close the communication with the PostgreSQL
cur.close()
conn.close()
print('Database connection closed.')


