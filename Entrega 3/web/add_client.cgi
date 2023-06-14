#!/usr/bin/python3
import cgi
form = cgi.FieldStorage()
cust_no = form.getvalue('cust_no')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Add customer</title>')
print('<link rel="stylesheet" href="styles.css">')
print('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">')
print('</head>')
print('<body>')
# Go back to index
print('<a href="clients.cgi"><span class="material-icons">')
print('arrow_back')
print('</span></a>')
# The string has the {}, the variables inside format() will replace the {}
print('<h3>Create customer</h3>')
# The form will send the info needed for the SQL query
print('<form action="insert_client.cgi" method="post">')
print('<p><input type="hidden" name="cust_no" value="{}"/></p>'.format(cust_no))
print('<p>Customer name: <input type="text" name="name"/></p>')
print('<p>Email: <input type="text" name="email"/></p>')
print('<p>Phone: <input type="text" name="phone"/></p>')
print('<p>Address: <input type="text" name="address"/></p>')
print('<p><input type="submit" value="Create customer"/></p>')
print('</form>')
print('</body>')
print('</html>')
