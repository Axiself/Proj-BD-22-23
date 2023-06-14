#!/usr/bin/python3
import psycopg2, cgi
import login
form = cgi.FieldStorage()

order_no = int(form.getvalue('order_no'))
cust_no = int(form.getvalue('cust_no'))
date = form.getvalue('date')

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

    # Go back to orders
    print('<a href="orders.cgi" class="arrow"><span class="material-icons">')
    print('arrow_back')
    print('</span></a>')

    # Making query
    sql = """
        START TRANSACTION;
        SET CONSTRAINTS ALL DEFERRED;
        INSERT INTO orders VALUES (%s, %s, %s);"""
    temp = [order_no, cust_no, date]

    # Adding qty inserts to query
    cursor.execute('SELECT sku FROM product;')
    result = cursor.fetchall()
    for row in result:
        qty = int(form.getvalue('{}'.format(row[0])))
        if(qty != 0):
            temp.append(order_no)
            temp.append(row[0])
            temp.append(qty)
            sql += 'INSERT INTO contains VALUES (%s, %s, %s);'
    sql += 'COMMIT;'

    data = tuple(temp)
    print('<p>Order added successfuly</p>')
    cursor.execute(sql, data)
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