import mysql.connector

# Database Connection Establishment
db = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='root', 
    database='medicalStore'
)