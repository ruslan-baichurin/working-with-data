import cgi
form = cgi.FieldStorage() # parse form data
print('Content-type: text/html\n')
print('<title>Reply Page</title>')
if not 'user' in form:
    print('<h1>Who are you?</h1>')
else:
    print(f"<h1>Hello <i>{cgi.escape(form['user'].value)}</i>!</h1>")