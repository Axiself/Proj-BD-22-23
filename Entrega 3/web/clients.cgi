#!/usr/bin/python3
import psycopg2
import login

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Customers</title>')
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
	sql = 'SELECT * FROM customer'
	cursor.execute(sql)
	result = cursor.fetchall()
	num = len(result)
	max = -1
	# Displaying customers
	print('<table border="3" cellspacing="5">')
	print('<tr>')
	print('<th>Customer Number</th>')
	print('<th>Name</th>')
	print('<th>Email</th>')
	print('<th>Phone</th>')
	print('<th>Address</th>')
	print('</tr>')
	for row in result:
		if(max <= row[0]):
			max = row[0]+1
		print('<tr>')
		for value in row:
			# The string has the {}, the variables inside format() will replace the {}
			print('<td>{}</td>'.format(value))
		print('<td><div class="center-content"><a href="delete_customer.cgi?cust_no={}"><span class="material-icons">delete</span></a></div></td>'.format(row[0]))
		print('</tr>')
	print('</table>')
	print('<a href="add_client.cgi?cust_no={}" class="button"><span class="material-icons">add</span>Add client</a>'.format(max))
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