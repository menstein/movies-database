from user import User
from database import Database

Database.initialize(database="Learning", host="localhost", user="postgres", password="r49n4r0k")

member = User(input("Insert EMAIL:"),input("Insert FIRSTNAME:"),input("Insert LASTNAME:"), None)

member.save_to_db()
