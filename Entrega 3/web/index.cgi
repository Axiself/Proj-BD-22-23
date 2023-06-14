#!/usr/bin/python3

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Index</title>')
print('<link rel="stylesheet" href="styles.css">')
print('</head>')
print('<body>')
print('<div class="container">')

print('<form action="products.cgi" method="GET">')
print('<input type="submit" value="Register, edit and remove products" class="button"/>')
print('</form>')

print('<form action="clients.cgi" method="GET">')
print('<input type="submit" value="Register and remove clients" class="button"/>')
print('</form>')

print('<form action="orders.cgi" method="GET">')
print('<input type="submit" value="Register orders" class="button"/>')
print('</form>')

print('<form action="suppliers.cgi" method="GET">') # Simular o pagamento de encomendas
print('<input type="submit" value="Register and remove suppliers" class="button"/>')
print('</form>')

print('<form action="simulate_orders.cgi" method="GET">') # Simular o pagamento de encomendas
print('<input type="submit" value="Simulate order payments" class="button"/>')
print('</form>')

print('</div>')
print('</body>')
print('</html>')