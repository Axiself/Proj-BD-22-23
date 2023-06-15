#!/usr/bin/python3
import psycopg2, cgi
import login
form = cgi.FieldStorage()

#getvalue uses the names from the form in previous page
TIN = form.getvalue('tin')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Delete supplier</title>')
print('<link rel="stylesheet" href="styles.css">')
print('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">')
print('</head>')
print('<body>')
connection = None
try:
	# Go back to suppliers
	print('<a href="suppliers.cgi?page=1" class="arrow"><span class="material-icons">')
	print('arrow_back')
	print('</span></a>')
	
	# Creating connection
	connection = psycopg2.connect(login.credentials)
	cursor = connection.cursor()
	
	# Making query
	sql = """
        DELETE FROM delivery WHERE TIN = %s;
        DELETE FROM supplier WHERE TIN = %s;"""
	data = (TIN, TIN)
	# The string has the {}, the variables inside format() will replace the {}
	print('<p>Supplier "{}" deleted.</p>'.format(TIN))
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