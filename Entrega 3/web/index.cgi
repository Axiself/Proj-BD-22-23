#!/usr/bin/python3

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Index</title>')
print('<link rel="stylesheet" href="styles.css">')
print('</head>')
print('<body>')
print('<div id="id1">')
print('<h1>Insert title here</h1>')
print('<form action="balance.cgi" method="GET">')
print('<p>New balance: <input type="text" name="balance"/></p>')
print('<input type="submit" value="Balance"/>')
print('</form>')
print('</div>')
print('</body>')
print('</html>')