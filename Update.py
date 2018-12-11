import connect

print('Search by id:')
id = input()

print('Edit name:')
name = input()
print('Edit address:')
address = input()


connect.mycursor.execute ("UPDATE customers SET name=%s, address=%s WHERE id=%s ", (name, address, id))

connect.mydb.commit()

print(connect.mycursor.rowcount, "record update.")