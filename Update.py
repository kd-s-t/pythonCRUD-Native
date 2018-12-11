import database.connect as connect

print('Search by id:')
id = input()

print('Edit name:')
name = input()

if name is "":
	print("Leaving name empty will update the value to empty as well.")

print('Edit address:')
address = input()

if address is "":
	print("Leaving address empty will update the value to empty as well.")

connect.mycursor.execute ("UPDATE customers SET name=%s, address=%s WHERE id=%s ", (name, address, id))

connect.mydb.commit()

print(connect.mycursor.rowcount, "record update.")