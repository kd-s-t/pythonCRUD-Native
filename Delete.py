import database.connect as connect

print('Search by id to delete:')
id = input()

connect.mycursor.execute ("DELETE FROM customers WHERE id = %s", (id,))

connect.mydb.commit()

print(connect.mycursor.rowcount, "record deleted.")