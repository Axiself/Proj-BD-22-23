#!/usr/bin/python3
import psycopg2, cgi
import login
form = cgi.FieldStorage()

#getvalue uses the names from the form in previous page
cust_no = form.getvalue('cust_no')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Delete customer</title>')
print('<link rel="stylesheet" href="styles.css">')
print('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">')
print('</head>')
print('<body>')
connection = None
try:
	# Go back to clients
	print('<a href="clients.cgi?page=1" class="arrow"><span class="material-icons">')
	print('arrow_back')
	print('</span></a>')
	# Creating connection
	connection = psycopg2.connect(login.credentials)
	cursor = connection.cursor()
	# Making query
	sql = """
	    DELETE FROM process WHERE order_no IN (SELECT order_no FROM orders WHERE cust_no = %s);
	    DELETE FROM contains WHERE order_no IN (SELECT order_no FROM orders WHERE cust_no = %s);
        DELETE FROM pay WHERE cust_no = %s;
	    DELETE FROM orders WHERE cust_no = %s;
        DELETE FROM customer WHERE cust_no = %s;"""
	data = (cust_no, cust_no, cust_no, cust_no, cust_no)
	# The string has the {}, the variables inside format() will replace the {}
	print('<p>Client "{}" deleted.</p>'.format(cust_no))
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