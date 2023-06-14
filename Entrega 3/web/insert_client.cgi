#!/usr/bin/python3
import psycopg2, cgi
import login
form = cgi.FieldStorage()

cust_no = int(form.getvalue('cust_no'))
cust_name = form.getvalue('name')
email = form.getvalue('email')
phone = form.getvalue('phone')
address = form.getvalue('address')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Add customer</title>')
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
    print('<a href="clients.cgi"><span class="material-icons">')
    print('arrow_back')
    print('</span></a>')

    # Making query
    sql = 'INSERT INTO customer VALUES (%s, %s, %s, %s, %s);'
    data = (cust_no, cust_name, email, phone, address)
    print('<p>Customer added successfuly</p>')
    cursor.execute(sql, data)
    connection.commit()
    
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