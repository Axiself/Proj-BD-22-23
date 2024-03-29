#!/usr/bin/python3
import psycopg2
import login, cgi
form = cgi.FieldStorage()

page = int(form.getvalue("page"))
page_size = 10

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Update or remove products</title>')
print('<link rel="stylesheet" href="styles.css">')
print('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">')
print('</head>')
print('<body>')

connection = None
try:
	# Creating connection
	connection = psycopg2.connect(login.credentials)
	cursor = connection.cursor()

	# Go back to index.cgi
	print('<a href="index.cgi" class="arrow"><span class="material-icons">')
	print('arrow_back')
	print('</span></a>')

	# Getting all products
	sql= 'SELECT * FROM product LIMIT %s OFFSET %s'
	data = (page_size+1, (page-1)*page_size)
	cursor.execute(sql, data)
	result = cursor.fetchall()
	size = len(result)

	# Displaying products
	print('<table border="3" cellspacing="5">')
	print('<tr>')
	print('<th>SKU</th>')
	print('<th>Product name</th>')
	print('<th>Description</th>')
	print('<th>Price</th>')
	print('<th>EAN</th>')
	print('</tr>')
	for row in result[:page_size]:
		print('<tr>')
		for value in row:
			print('<td>{}</td>'.format(value))
		print('<td><div class="center-content"><a href="edit_product.cgi?sku={}"><span class="material-icons">edit</span></a></div></td>'.format(row[0]))
		print('<td><div class="center-content"><a href="delete_product.cgi?sku={}"><span class="material-icons">delete</span></a></div></td>'.format(row[0]))
		print('</tr>')
	print('</table>')

	print('<div class="page-bottom">')
	print('<a href="add_product-supplier.cgi" class="button"><span class="material-icons">add</span>Add product</a>')

	print('<div class="pagination">')
	# Prev page
	if(page > 1):
		print('<a href="products.cgi?page={}" class="page-arrow"><span class="material-icons">'.format(page-1))
		print('arrow_back')
		print('</span></a>')

	# Current page
	print('<h3 style="margin: 10px; margin-top: 16px">Page {}</h3>'.format(page))

	# Next page
	if(size == page_size+1):
		print('<a href="products.cgi?page={}" class="page-arrow"><span class="material-icons">'.format(page+1))
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