#!/usr/bin/python3
import psycopg2
import login

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Make an order</title>')
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
	print('<a href="index.cgi" class="arrow"><span class="material-icons">')
	print('arrow_back')
	print('</span></a>')
	# Making query
	sql= """
		SELECT a.order_no, b.cust_no, b.name, total_price, date
		FROM(
    		SELECT order_no, SUM(price*qty) as total_price
    		FROM product NATURAL JOIN contains
    		GROUP BY order_no
		) as a NATURAL JOIN orders NATURAL JOIN customer AS b;"""
	
	cursor.execute(sql)
	result = cursor.fetchall()
	num = len(result)
	max_orders = -1
	# Displaying orders
	print('<table border="3" cellspacing="5">')
	print('<tr>')
	print('<th>Order Number</th>')
	print('<th>Customer Number</th>')
	print('<th>Customer Name</th>')
	print('<th>Total Price</th>')
	print('<th>Date</th>')
	print('</tr>')
	for row in result:
		if(max_orders <= row[0]):
			max_orders = row[0]+1
		print('<tr>')
		for value in row:
			# The string has the {}, the variables inside format() will replace the {}
			print('<td>{}</td>'.format(value))
		print('</tr>')
	print('</table>')

	print('<td><a href="add_order.cgi?order_no={}" class="button"><span class="material-icons">add</span>Add Order</a></td>'.format(max_orders))
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