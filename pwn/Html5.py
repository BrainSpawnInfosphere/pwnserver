#!/usr/bin/env python

class Base(object):
	"""
	"""
	def write(self, filename):
		print('need to enable writing')


class CSS(Base):
	"""
	"""
	@staticmethod
	def basic():
		basic = """
		body {
			background-color: white;
		}

		h1 {
			color: black;
			text-align: center;
		}

		p {
			font-family: verdana;
			font-size: 20px;
		}
		"""
		return basic

	@staticmethod
	def cssTable(color='#dddddd'):
		css = """
		table {
			font-family: arial, sans-serif;
			border-collapse: collapse;
			width: 100%;
			}
		td, th {
			border: 1px solid #dddddd;
			text-align: left;
			padding: 8px;
		}
		tr:nth-child(even) {
			background-color: COLOR;
		}"""
		return css.replace('COLOR', color)

	@staticmethod
	def cssToolTip(width=200):
		css = """
		.tooltip {
		    position: relative;
		    display: inline-block;
		    border-bottom: 1px dotted black;
		}

		.tooltip .tooltiptext {
		    visibility: hidden;
		    width: TEXT_WIDTH;
		    background-color: #555;
		    color: #fff;
		    text-align: center;
		    border-radius: 6px;
		    padding: 5px 0;
		    position: absolute;
		    z-index: 1;
		    bottom: 125%;
		    left: 50%;
		    margin-left: TEXT_OFFSET;
		    opacity: 0;
		    transition: opacity 1s;
		}

		.tooltip .tooltiptext::after {
		    content: "";
		    position: absolute;
		    top: 100%;
		    left: 50%;
		    margin-left: -5px;
		    border-width: 5px;
		    border-style: solid;
		    border-color: #555 transparent transparent transparent;
		}

		.tooltip:hover .tooltiptext {
		    visibility: visible;
		    opacity: 1;
		}
		"""
		css = css.replace('TEXT_WIDTH', str(width)+'px')
		css = css.replace('TEXT_OFFSET', str(-width/2)+'px')
		# css = css.replace('TEXT_WIDTH', '400px')
		# css = css.replace('HALF_TEXT_WIDTH', '-400px')
		return css


class HTML(Base):
	"""
	"""
	def __init__(self):
		# self.page = '<!DOCTYPE html><html><body></body></html>'
		# self.parts = ['<!DOCTYPE html>', '<html>', '<head>', '</head>', '<body>', '</body>', '</html>']
		# pass
		self.clear()

	def clear(self):
		self.parts = ['<!DOCTYPE html>', '<html>', '<head>', '<style>', '</style>', '</head>', '<body>', '</body>', '</html>']

	def css(self, css, bgcolor=None):
		if bgcolor:
			n = self.find('</style>')
			if n:
				self.parts.insert(n, 'body {background-color: {};}'.format(bgcolor))
		if css:
			n = self.find('</style>')
			if n:
				self.parts.insert(n, css)

	def find(self, token):
		cnt = 0
		for tag in self.parts:
			if tag == token:
				return cnt
				break
			cnt += 1
		return None

	@staticmethod
	def tooltip(text, popup_text):
		return '<div class="tooltip">{}<span class="tooltiptext">{}</span></div>'.format(text, popup_text)

	def linuxFont(self):
		n = self.find('</head>')
		if n:
			self.parts.insert(n, '<link href="https://cdn.rawgit.com/walchko/font-linux/v0.6/assets/font-linux.css" rel="stylesheet">')

	def h1(self, string):
		n = self.find('</body>')
		if n:
			self.parts.insert(n, '<h1>{}</h1>'.format(string))

	def h2(self, string):
		n = self.find('</body>')
		if n:
			self.parts.insert(n, '<h2>{}</h2>'.format(string))

	def h3(self, string):
		n = self.find('</body>')
		if n:
			self.parts.insert(n, '<h3>{}</h3>'.format(string))

	def p(self, string):
		n = self.find('</body>')
		if n:
			self.parts.insert(n, '<p>{}</p>'.format(string))

	def javascript(self, code):
		n = self.find('</body>')
		if n:
			self.parts.insert(n, '<script>{}</script>'.format(code))

	def cssLink(self, css):
		n = self.find('</head>')
		if n:
			self.parts.insert(n, '<link rel="stylesheet" href="{}}">'.format(css))

	def table(self, table, class_name=None):
		# n = self.find('</style>')
		# if n:
		# 	if not self.table_css:
		# 		self.parts.insert(n, self.table_format.replace("COLOR", self.table_color))
		# 		self.table_css = True

		n = self.find('</body>')
		if n:
			if class_name:
				self.parts.insert(n, '<table class={}>'.format(class_name))
			else:
				self.parts.insert(n, '<table>')
			# offset = 1
			for offset, line in enumerate(table):
				# self.parts.insert(n+offset, ''.join(map(str, line)))
				s = map(str, line)
				# self.parts.insert(n+offset, ''.join())
				l = '<tr>'
				for i in s:
					l += '<td>' + i + '</td>'
				l += '</tr>'
				self.parts.insert(n+offset+1, l)
				# offset += 1
			self.parts.insert(n+offset+2, '</table>')

	def img(self, image, w=None, h=None):
		n = self.find('</body>')
		if n:
			if w and h:
				self.parts.insert(n, '<img src="{}" alt="img" width="{}" height="{}">'.format(image, w, h))
			elif w:
				self.parts.insert(n, '<img src="{}" alt="img" width="{}">'.format(image, w))
			else:
				self.parts.insert(n, '<img src="{}" alt="img">'.format(image))

	def iframe(self, image, w=None, h=None):
		n = self.find('</body>')
		if n:
			if w and h:
				self.parts.insert(n, '<iframe src="{}" alt="img" width="{}" height="{}">'.format(image, w, h))
			elif w:
				self.parts.insert(n, '<iframe src="{}" alt="img" width="{}">'.format(image, w))
			else:
				self.parts.insert(n, '<iframe src="{}" alt="img">'.format(image))

	def footer(self, string):
		n = self.find('</body>')
		if n:
			self.parts.insert(n, '<footer>{}</footer>'.format(string))

	def __str__(self):
		# print self.parts
		return ''.join(self.parts)
		# return str(self.parts)

	def __repr__(self):
		return self.__str__()


def main():
	css = """
	footer {
		padding: 1em;
		color: white;
		background-color: black;
		clear: left;
		text-align: center;
	}
	"""
	css += CSS.cssTable()
	html = HTML()
	html.css(css)
	html.p('this is a test')
	html.p('second line')
	html.p('third line')
	html.table([['kw@hotmail.com', 'Good', ''], ['hw@hotmail.com', 'Bad', '20 Sept 2014']], 'myClass')
	# html.table([['/mnt', '22GB'],['/', '123 GB']])
	html.p('this is fun!')
	# html.table([['a','b'], [1,2], [3,4]])
	# html.iframe('http://giphy.com/embed/8w8cs5IcECPg4', 400, 400)
	html.img('http://www.walldevil.com/wallpapers/w11/78194-women-boobs.jpg', 400)
	html.footer('<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" />')
	print html

if __name__ == '__main__':
	main()
