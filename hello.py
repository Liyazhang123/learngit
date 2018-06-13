from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.flag = False
		
	def handle_data(self,data):
		if self.lasttag == 'p':
			print("Encountered p data :",data)
	
	def _attr(attrlist, attrname):
		for attr in attrlist:
			if attr[0] == attrname:
				return attr[1]
		return None
	

	def handle_starttag(self, tag, attrs):
		if tag == 'p' and _attr(attrs, 'class') == 'p_font':
			self.flag = True
			


parser = MyHTMLParser()
parser.feed('''<html>
    <head>
        <title>Test</title>
    </head>
    <body>
        <h1>Parse me!</h1>
        <img src = "" />
        <p>A paragraph.</p>
                <p class = "p_font">A paragraph with class.</p>
                <!-- comment -->
        <div>
            <p>A paragraph in div.</p>
        </div>
    </body>
</html>''')
