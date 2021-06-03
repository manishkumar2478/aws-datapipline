import psycopg2

conn = psycopg2.connect(
        host="127.0.0.1",
    database="BSENSE",
    user="postgres",
    password="Admin@123"
)
print ("Opened database successfully")
curr = conn.cursor()
curr.execute("INSERT INTO bse.COMPANY (ID,NAME,AGE,ADDRESS,SALARY)VALUES(3, 'Manish', 32, 'California', 20000.00 )");
curr.execute("INSERT INTO bse.COMPANY (ID,NAME,AGE,ADDRESS,SALARY)VALUES(4, 'Harsh', 25, 'Texas', 15000.00 )");
conn.commit()
print ("Records created successfully");
conn.close()