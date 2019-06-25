import MySQLdb

# Open database connection
db = MySQLdb.connect(host='localhost',
                    database='db',
                    user='root',
                    password='1234',)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO WEATHER(
         CITY,TEMPERATURE)
         VALUES ('VIJAYAWADA', 34.5),('VIZAG', 31.4 ),('HYDERABAD', 42.5)"""
try:
   
   cursor.execute(sql)
   
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
