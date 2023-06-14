#!/usr/bin/python3
import cgi
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

# Go back to index
print('<a href="products.cgi"><span class="material-icons">')
print('arrow_back')
print('</span></a>')

print('<h3>Create product-supplier pair</h3>')
# Creating the form
print('<form action="insert_product-supplier.cgi" method="post">')
# Product form
print('<h4>Product form:</h4>')
print('<p>SKU: <input type="text" name="sku"/></p>')
print('<p>Product name: <input type="text" name="p_name"/></p>')
print('<p>Description: <input type="text" name="description"/></p>')
print('<p>Price: <input type="text" name="price"/></p>')
print('<p>EAN code: <input type="text" name="ean"/></p>')

# Supplier form
print('<h4>Supplier form:</h4>')
print('<p>TIN: <input type="text" name="TIN"/></p>')
print('<p>Supplier name: <input type="text" name="s_name"/></p>')
print('<p>Address: <input type="text" name="address"/></p>')
print('<p>Date: <input type="date" name="date"/></p>')
print('<p><input type="submit" value="Create product-supplier pair"/></p>')
print('</form>')

print('</body>')
print('</html>')