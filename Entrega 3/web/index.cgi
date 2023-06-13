#!/usr/bin/python3

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Index</title>')
print('<link rel="stylesheet" href="styles.css">')
print('</head>')
print('<body>')
print('<div class="container">')

print('<form action="product_supplier.cgi" method="GET">') # Registar e remover produtos e fornecedores
print('<input type="submit" value="Registar e remover produtos e fornecedores" class="button"/>')
print('</form>')

print('<form action="price_description.cgi" method="GET">') # Alterar preços de produtos e respectivas descrições
print('<input type="submit" value="Alterar preços de produtos e respectivas descrições" class="button"/>')
print('</form>')

print('<form action="clients.cgi" method="GET">') # Registar e remover clientes
print('<input type="submit" value="Registar e remover clientes" class="button"/>')
print('</form>')

print('<form action="orders.cgi" method="GET">') # Realizar encomendas
print('<input type="submit" value="Realizar encomendas" class="button"/>')
print('</form>')

print('<form action="simulate_orders.cgi" method="GET">') # Simular o pagamento de encomendas
print('<input type="submit" value="Simular o pagamento de encomendas" class="button"/>')
print('</form>')

print('</div>')
print('</body>')
print('</html>')