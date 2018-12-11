import connect

print('Enter your name:')
name = input()
print('Enter your address:')
address = input()

val = (name, address)
connect.mycursor.execute("INSERT INTO customers (name, address) VALUES (%s, %s)", val)

connect.mydb.commit()

print(connect.mycursor.rowcount, "record inserted.")