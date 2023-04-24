import pymysql
from core import mysqlConnector


db = mysqlConnector()
db.showDatabase("acti")
db.insertUser("test","66894523")