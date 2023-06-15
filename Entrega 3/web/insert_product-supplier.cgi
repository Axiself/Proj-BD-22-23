#!/usr/bin/python3
import psycopg2, cgi
import login
form = cgi.FieldStorage()

sku = form.getvalue('sku')
p_name = form.getvalue('p_name')
description = form.getvalue('description')
price = float(form.getvalue('price'))
ean = form.getvalue('ean')
if(ean != None):
    ean = int(ean)
TIN = form.getvalue('TIN')
s_name = form.getvalue('s_name')
address = form.getvalue('address')
date = form.getvalue('date')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Add product-supplier pair</title>')
print('<link rel="stylesheet" href="styles.css">')
print('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">')
print('</head>')
print('<body>')

connection = None
try:
	# Creating connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    # Go back to products
    print('<a href="products.cgi?page=1" class="arrow"><span class="material-icons">')
    print('arrow_back')
    print('</span></a>')

    # Making query
    sql = """
        INSERT INTO product VALUES (%s, %s, %s, %s, %s);
        INSERT INTO supplier VALUES (%s, %s, %s, %s, %s);"""
    data = (sku, p_name, description, price, ean, 
            TIN, s_name, address, sku, date)
    print('<p>Order and product added successfuly</p>')
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