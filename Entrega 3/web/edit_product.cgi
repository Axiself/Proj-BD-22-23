#!/usr/bin/python3
import cgi
form = cgi.FieldStorage()

sku = form.getvalue('sku')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Edit product</title>')
print('<link rel="stylesheet" href="styles.css">')
print('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">')
print('</head>')
print('<body>')

# Go back to index
print('<a href="products.cgi"><span class="material-icons">')
print('arrow_back')
print('</span></a>')

# Creating the form
print('<h3>Edit product "{}"</h3>'.format(sku))
print('<form action="update_product.cgi" method="post">')
print('<p><input type="hidden" name="sku" value="{}"/></p>'.format(sku))
print('<p>Description: <input type="text" name="description"/></p>')
print('<p>Price: <input type="text" name="price"/></p>')
print('<p><input type="submit" value="Update product"/></p>')
print('</form>')

print('</body>')
print('</html>')