#!/usr/bin/python3
import cgi
form = cgi.FieldStorage()
cust_no = form.getvalue('cust_no')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Add client</title>')
print('<link rel="stylesheet" href="styles.css">')
print('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">')
print('</head>')
print('<body>')
# Go back to clients.cgi
print('<a href="clients.cgi?page=1" class="arrow"><span class="material-icons">')
print('arrow_back')
print('</span></a>')

# Creating the form
print('<h3>Create customer</h3>')
print('<form action="insert_client.cgi" method="post">')
print('<div class="form-field">')
print('<p><input type="hidden" name="cust_no" value="{}"/>'.format(cust_no))
print('<p>Customer name: </p><input type="text" name="name"/>')
print('<p>Email: </p><input type="text" name="email"/>')
print('<p>Phone: </p><input type="text" name="phone"/>')
print('<p>Address: </p><input type="text" name="address"/>')
print('</div>')
print('<p><input type="submit" value="Create customer"/></p>')
print('</form>')
print('</body>')
print('</html>')
