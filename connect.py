import MySQLdb

# Open database connection
db = MySQLdb.connect(host='localhost',
                    database='db',
                    user='root',
                    password='1234',
                    ) 

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS WEATHER")

# Create table as per your requirement
sql = """CREATE TABLE WEATHER (
        
         CITY CHAR(20) NOT NULL,
	 TEMPERATURE FLOAT(20) NOT NULL
          )"""

cursor.execute(sql)

# disconnect from server
db.close()
