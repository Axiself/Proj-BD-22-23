#!/usr/bin/python3
import psycopg2,cgi
import login
form = cgi.FieldStorage()
order_no = form.getvalue('order_no')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Add order</title>')
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
    print('<a href="suppliers.cgi" class="arrow"><span class="material-icons">')
    print('arrow_back')
    print('</span></a>')
    
    # The string has the {}, the variables inside format() will replace the {}
    print('<h3>Create supplier</h3>')

    # Creating query to get all products
    sql = 'SELECT * FROM product;'
    cursor.execute(sql)
    result = cursor.fetchall()
    len = len(result)

    # Creating the form
    print('<form action="insert_supplier.cgi" method="post">')
    print('<div class="form-field>')
    print('<p>TIN: </p><input type="text" name="tin"/>')
    print('<p>Supplier name: </p><input type="text" name="name"/>')
    print('<p>Address: </p><input type="text" name="address"/>')
    print('<p>SKU: </p><select name="sku">')
    for row in result:
        print('<option value="{}">{}, {}</option>'.format(row[0], row[0], row[1]))
    print('</select></p>')
    print('<p>Date: </p><input type="date" name="date"/>')
    print('</div>')
    print('<p><input type="submit" value="Create product-supplier pair"/></p>')
    print('</form>')
    
    # Redirect to product-supplier pair
    print('<a href="add_product-supplier.cgi">If looking to create a new product supplier pair, go here</a>')

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