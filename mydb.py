import mysql.connector
dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Tienalo123?'
    
)

cursorObject=dataBase.cursor()
cursorObject.execute("CREATE DATABASE QLPMT")
print("ok")