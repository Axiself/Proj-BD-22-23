#!/usr/bin/python3
import psycopg2
import login

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Orders to be payed</title>')
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
	print('<a href="index.cgi"><span class="material-icons">')
	print('arrow_back')
	print('</span></a>')

	print('<h1>Non Payed Orders</h1>')
	# Making query
	sql='SELECT * FROM orders WHERE order_no NOT IN (SELECT order_no FROM pay)'
	cursor.execute(sql)
	result = cursor.fetchall()

	# Display orders to be payed
	print('<table border="3" cellspacing="5">')
	print('<tr>')
	print('<th>Order number</th>')
	print('<th>Customer number</th>')
	print('<th>Date</th>')
	print('</tr>')
	for row in result:
		print('<tr>')
		for value in row:
			# The string has the {}, the variables inside format() will replace the {}
			print('<td>{}</td>'.format(value))
		print('<td><a href="pay_order.cgi?order_no={}&cust_no={}">Pay</a></td>'.format(row[0], row[1]))
		print('</tr>')
	print('</table>')

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