#!/usr/bin/python3
import psycopg2, cgi
import login
form = cgi.FieldStorage()

sku = form.getvalue('sku')
description = form.getvalue('description')
price = form.getvalue('price')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Update product</title>')
print('<link rel="stylesheet" href="styles.css">')
print('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">')
print('</head>')
print('<body>')

connection = None
try:
	# Creating connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    # Go back to index
    print('<a href="products.cgi"><span class="material-icons">')
    print('arrow_back')
    print('</span></a>')

    # Making query
    sql = 'UPDATE product SET description = %s, price = %s WHERE sku = %s;'
    data = (description, price, sku)
    print('<p>Product "{}" updated successfuly</p>'.format(sku))
    cursor.execute(sql, data)
    connection.commit()
    
    # Closing connection
    cursor.close()
except Exception as e:
	# Print errors on the webpage if they occur
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))
finally:
    if connection is not None:
	    connection.close()
print('</body>')
print('</html>')