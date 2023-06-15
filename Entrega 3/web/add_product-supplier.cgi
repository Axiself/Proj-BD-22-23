#!/usr/bin/python3
import cgi
form = cgi.FieldStorage()
order_no = form.getvalue('order_no')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Add product-supplier</title>')
print('<link rel="stylesheet" href="styles.css">')
print('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">')
print('</head>')
print('<body>')

# Go back to products
print('<a href="products.cgi?page=1" class="arrow"><span class="material-icons">')
print('arrow_back')
print('</span></a>')

print('<h3>Create product-supplier pair</h3>')
# Creating the form
print('<form action="insert_product-supplier.cgi" method="post">')
# Product form
print('<div class="form-field">')
print('<h4>Product form:</h4>')
print('<p>SKU: </p><input type="text" name="sku"/>')
print('<p>Product name: </p><input type="text" name="p_name"/>')
print('<p>Description: </p><input type="text" name="description"/>')
print('<p>Price: </p><input type="text" name="price"/>')
print('<p>EAN code: </p><input type="text" name="ean"/>')

# Supplier form
print('<h4>Supplier form:</h4>')
print('<p>TIN: </p><input type="text" name="TIN"/>')
print('<p>Supplier name: </p><input type="text" name="s_name"/>')
print('<p>Address: </p><input type="text" name="address"/>')
print('<p>Date: </p><input type="date" name="date"/>')
print('</div>')
print('<p><input type="submit" value="Create product-supplier pair"/>')
print('</form>')

print('</body>')
print('</html>')