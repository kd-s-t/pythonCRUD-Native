import database.connect as connect

connect.mycursor.execute("SELECT * FROM customers")

myresult = connect.mycursor.fetchall()

for x in myresult:
  print(x)