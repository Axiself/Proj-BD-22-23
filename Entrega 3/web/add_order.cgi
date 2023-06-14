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
    print('<a href="orders.cgi"><span class="material-icons">')
    print('arrow_back')
    print('</span></a>')
    
    # The string has the {}, the variables inside format() will replace the {}
    print('<h3>Create order</h3>')

    # Making query
    sql1 = 'SELECT cust_no, name FROM customer;'
    cursor.execute(sql1)
    result1 = cursor.fetchall()
 
    sql2 = 'SELECT sku, name FROM product;'
    cursor.execute(sql2)
    result2 = cursor.fetchall()

    # The form will send the info needed for the SQL query
    print('<form action="insert_order.cgi" method="post">')
    print('<p><input type="hidden" name="order_no" value="{}"/></p>'.format(order_no))
    print('<p>Customer: <select name="cust_no">')
    for row in result1:
        print('<option value="{}">{}, {}</option>'.format(row[0], row[0], row[1]))
    print('</select></p>')
    print('<p>Date: <input type="date" name="date"/></p>')
    for row in result2:
        print('<p>{} quantity: <input type="text" name="{}"/></p>'.format(row[0], row[0]))
    print('<p><input type="submit" value="Create order"/></p>')
    print('</form>')
    
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
