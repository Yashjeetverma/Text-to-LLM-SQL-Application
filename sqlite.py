import sqlite3

## Connect to Sqlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record, create table

cursor=connection.cursor()

#create the table
table_info="""

 Create Table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
  SECTION VARCHAR(25),MARKS INT);


"""
# When you edit in your database then you have to delete old database
# and create new database using python sqlite.py
# and by run this code write streamlit run sql.py
cursor.execute(table_info)

## Insert Some More records 

cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Darius','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Vikas','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')

# Displaying All the records 

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)
    
## Commit your changes in the database
connection.commit()
connection.close()