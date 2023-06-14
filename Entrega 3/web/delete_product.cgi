#!/usr/bin/python3
import psycopg2, cgi
import login
form = cgi.FieldStorage()

#getvalue uses the names from the form in previous page
sku = form.getvalue('sku')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Delete product</title>')
print('<link rel="stylesheet" href="styles.css">')
print('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">')
print('</head>')
print('<body>')
connection = None
try:
	# Go back to products
	print('<a href="products.cgi" class="arrow"><span class="material-icons">')
	print('arrow_back')
	print('</span></a>')
	# Creating connection
	connection = psycopg2.connect(login.credentials)
	cursor = connection.cursor()
	# Making query
	sql = """
        DELETE FROM delivery WHERE TIN IN (SELECT TIN FROM supplier WHERE sku = %s);
	    DELETE FROM supplier WHERE sku = %s;
	    DELETE FROM contains WHERE sku = %s;
	    DELETE FROM product WHERE sku = %s;"""
	data = (sku, sku, sku, sku)
	# The string has the {}, the variables inside format() will replace the {}
	print('<p>Product "{}" and its supplier(s) deleted.</p>'.format(sku))
	# Feed the data to the SQL query as follows to avoid SQL injection
	cursor.execute(sql, data)
	# Commit the update (without this step the database will not change)
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