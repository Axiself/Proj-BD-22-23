#!/usr/bin/python3
import psycopg2, cgi
import login
form = cgi.FieldStorage()

TIN = form.getvalue('tin')
name = form.getvalue('name')
address = form.getvalue('address')
sku = form.getvalue('sku')
date = form.getvalue('date')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Add supplier</title>')
print('<link rel="stylesheet" href="styles.css">')
print('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">')
print('</head>')
print('<body>')

connection = None
try:
	# Creating connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    # Go back to suppliers
    print('<a href="suppliers.cgi?page=1" class="arrow"><span class="material-icons">')
    print('arrow_back')
    print('</span></a>')

    # Making query
    sql = 'INSERT INTO supplier VALUES (%s, %s, %s, %s, %s);'
    data = (TIN, name, address, sku, date)
    print('<p>Supplier added successfuly</p>')
    cursor.execute(sql, data)
    connection.commit()

    # Closing connection
    cursor.close()
except Exception as e:
	# Print errors on the webpage if they occur
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))
    connection.rollback()
finally:
    if connection is not None:
	    connection.close()
print('</body>')
print('</html>')