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

# Go back to products
print('<a href="products.cgi" class="arrow"><span class="material-icons">')
print('arrow_back')
print('</span></a>')

# Creating the form
print('<h3>Edit product "{}"</h3>'.format(sku))
print('<form action="update_product.cgi" method="post">')
print('<div class="form-field>')
print('<input type="hidden" name="sku" value="{}"/>'.format(sku))
print('<p>Description: </p><input type="text" name="description"/>')
print('<p>Price: </p><input type="text" name="price"/>')
print('</div>')
print('<input type="submit" value="Update product"/>')
print('</form>')

print('</body>')
print('</html>')