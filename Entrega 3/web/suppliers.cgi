#!/usr/bin/python3
import psycopg2
import login, cgi
form = cgi.FieldStorage()

page = int(form.getvalue("page"))
page_size = 10

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Add or remove suppliers</title>')
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

    # Getting all suppliers
	sql= 'SELECT * FROM supplier LIMIT %s OFFSET %s'
	data = (page_size, (page-1)*page_size)
	cursor.execute(sql)
	result = cursor.fetchall()
	num = len(result)
	# Displaying products
	print('<table border="3" cellspacing="5">')
	print('<tr>')
	print('<th>TIN</th>')
	print('<th>Supplier name</th>')
	print('<th>Morada</th>')
	print('<th>SKU</th>')
	print('<th>Date</th>')
	print('</tr>')
	for row in result:
		print('<tr>')
		for value in row:
			# The string has the {}, the variables inside format() will replace the {}
			print('<td>{}</td>'.format(value))
		print('<td><div class="center-content"><a href="delete_supplier.cgi?tin={}"><span class="material-icons">delete</span></a></div></td>'.format(row[0]))
		print('</tr>')
	print('</table>')

	print('<div class="page-bottom">')
	print('<a href="add_supplier.cgi" class="button"><span class="material-icons">add</span>Add supplier</a>')

	print('<div class="pagination">')
	# Prev page
	if(page > 1):
		print('<a href="suppliers.cgi?page={}" class="page-arrow"><span class="material-icons">'.format(page-1))
		print('arrow_back')
		print('</span></a>')

	# Current page
	print('<h3 style="margin: 10px; margin-top: 16px">Page {}</h3>'.format(page))

	# Next page
	sql = 'SELECT TIN FROM supplier LIMIT %s OFFSET %s'
	data = (page_size, page*page_size)
	cursor.execute(sql)
	result = cursor.fetchall()
	size = len(result)
	if(size != 0):
		print('<a href="suppliers.cgi?page={}" class="page-arrow"><span class="material-icons">'.format(page+1))
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