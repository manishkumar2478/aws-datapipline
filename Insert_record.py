import psycopg2

conn = conn = psycopg2.connect(   
    host="127.0.0.1",
    database="BSENSE",
    user="postgres",
    password="Admin@123"
    )
		
print ("Opened database successfully")

cur = conn.cursor()
cur.execute('''CREATE TABLE bse.COMPANY
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL);''')
print ("Table created successfully")

conn.commit()
conn.close()