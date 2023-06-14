#!/usr/bin/python3
import psycopg2, cgi
import login
form = cgi.FieldStorage()

#getvalue uses the names from the form in previous page
order_no = int(form.getvalue('order_no'))
cust_no = int(form.getvalue('cust_no'))

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Payment proccess</title>')
print('<link rel="stylesheet" href="styles.css">')
print('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">')
print('</head>')
print('<body>')
connection = None
try:
	# Creating connection
	connection = psycopg2.connect(login.credentials)
	cursor = connection.cursor()

	# Go back to simulate_orders
	print('<a href="simulate_orders.cgi" class="arrow"><span class="material-icons">')
	print('arrow_back')
	print('</span></a>')

	# Making query
	sql='INSERT INTO pay VALUES (%s, %s);'
	data = (order_no, cust_no)
	cursor.execute(sql, data)
	connection.commit()

	# The string has the {}, the variables inside format() will replace the {}
	print('<p>Order "{}" has been payed.</p>'.format(order_no))

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