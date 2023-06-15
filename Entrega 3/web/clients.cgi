#!/usr/bin/python3
import psycopg2
import login, cgi
form = cgi.FieldStorage()

page = int(form.getvalue("page"))
page_size = 10

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

	# Getting the next cust_no
	sql = 'SELECT cust_no FROM customer'
	cursor.execute(sql)
	result = cursor.fetchall()
	max = -1
	for row in result:
		if(max <= row[0]):
				max = row[0]+1

	# Making query
	sql = 'SELECT * FROM customer LIMIT %s OFFSET %s'
	data = (page_size+1, (page-1)*page_size)
	cursor.execute(sql, data)
	result = cursor.fetchall()
	size = len(result)
	
	# Displaying customers
	print('<table border="3" cellspacing="5">')
	print('<tr>')
	print('<th>Customer Number</th>')
	print('<th>Name</th>')
	print('<th>Email</th>')
	print('<th>Phone</th>')
	print('<th>Address</th>')
	print('</tr>')
	for row in result[:page_size]:
		print('<tr>')
		for value in row:
			# The string has the {}, the variables inside format() will replace the {}
			print('<td>{}</td>'.format(value))
		print('<td><div class="center-content"><a href="delete_client.cgi?cust_no={}"><span class="material-icons">delete</span></a></div></td>'.format(row[0]))
		print('</tr>')
	print('</table>')

	print('<div class="page-bottom">')
	print('<a href="add_client.cgi?cust_no={}" class="button"><span class="material-icons">add</span>Add client</a>'.format(max))

	print('<div class="pagination">')
	# Prev page
	if(page > 1):
		print('<a href="clients.cgi?page={}" class="page-arrow"><span class="material-icons">'.format(page-1))
		print('arrow_back')
		print('</span></a>')

	# Current page
	print('<h3 style="margin: 10px; margin-top: 16px">Page {}</h3>'.format(page))

	# Next page
	if(size == page_size+1):
		print('<a href="clients.cgi?page={}" class="page-arrow"><span class="material-icons">'.format(page+1))
		print('arrow_forward')
		print('</span></a>')
	print('</div>')
	print('</div>')

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