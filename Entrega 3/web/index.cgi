#!/usr/bin/python3

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Index</title>')
print('<link rel="stylesheet" href="styles.css">')
print('</head>')
print('<body style="display: flex; flex-direction: column; align-items: center">')
print('<h1> Projeto BD 2022/2023 </h1>')
print('<div class="index-menu">')

# Creating index buttons
print('<form action="products.cgi?page=1" method="POST">')
print('<input type="submit" value="Register, edit and remove products" class="button"/>')
print('</form>')

print('<form action="clients.cgi?page=1" method="POST">')
print('<input type="submit" value="Register and remove clients" class="button"/>')
print('</form>')

print('<form action="orders.cgi?page=1" method="POST">')
print('<input type="submit" value="Register orders" class="button"/>')
print('</form>')

print('<form action="suppliers.cgi?page=1" method="POST">')
print('<input type="submit" value="Register and remove suppliers" class="button"/>')
print('</form>')

print('<form action="simulate_orders.cgi?page=1" method="POST">')
print('<input type="submit" value="Simulate order payments" class="button"/>')
print('</form>')

print('</div>')
print('</body>')
print('</html>')