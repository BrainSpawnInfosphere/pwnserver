#!/usr/bin/env python


from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from socket import gethostname
import time
import argparse
from Html5 import HTML, CSS
import pwn
import threading

"""
This implements the main server code.
"""

class PwmThread(threading.Thread):
	def __init__(self, filename):
		threading.Thread.__init__(self)
		self.json = filename

	def run(self):
		"""
		pwn_results.json
		{
			'date': 'last time updated',
			'bob': [
				{
					'email': 'bob@gmail.com':
					'status': True,
					'BreachDate': '',
					'Description': '',
					'Domain': ''
				},
				{
					'email': bob@yahoo.com',
					'status': False
				}
			]
			'tom': [ ... ]
			'sam': [ ... ]
		}
		time.strftime('%H%M on %A %-d %B %Y')
		"""
		while True:
			accounts = pwn.readJson(self.json)
			results = {}
			results['date'] = time.strftime('%H%M on %A %-d %B %Y')
			print('<<<<<<<<< checking >>>>>>>>>>>>>>')
			for person, array in accounts.items():
				results[person] = []
				for email in array:
					ret, data = pwn.isBreach(email)
					# ans = []
					if ret:
						for entry in data:
							results[person].append({'email': email, 'status': True, 'Domain': entry['Domain'], 'BreachDate': entry['BreachDate'], 'Description': entry['Description']})
					else:
						results[person].append({'email': email, 'status': False})

					# for i in ans:
					# 	results[person].append(i)

					time.sleep(2)

			pwn.writeJson('pwn_results.json', results)

			print('Updated and save to json file')

			time.sleep(12*3600)


class ServerHandler(BaseHTTPRequestHandler):
	"""
	"""
	def do_GET(self):
		# print 'connection from:', self.address_string()

		if self.path == '/':
			# hn = self.server.server_address[0]
			# pt = self.server.server_address[1]
			# print self.server.server_address
			info = pwn.readJson('pwn_results.json')
			# print 'info', info

			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()

			css = """
				body {
					background-color: white;
				}

				h1 {
					color: black;
					text-align: center;
				}

				h3 {
					color: gray;
					text-align: center;
				}

				p {
					font-family: verdana;
					font-size: 20px;
				}

				a:link {
				    color: gray;
				}

				a:visited {
				    color: gray;
				}

				a:hover {
				    color: white;
				}

				footer {
					padding: 1em;
					color: white;
					background-color: black;
					clear: left;
					text-align: center;
				}
			"""
			css += CSS.cssTable()
			css += CSS.cssToolTip(400)  # set tooltip box width 400px
			# print css

			html = HTML()
			html.css(css)
			html.linuxFont()
			html.h1('Username and Password Status')
			html.h3('Last updated: {}'.format(info['date']))
			info.pop('date')
			for person, array in info.items():
				html.h2(person)
				table = []
				for results in array:
					if results['status']:
						row = [results['email'], HTML.tooltip('breached', results['Description']), results['BreachDate'], results['Domain']]
					else:
						row = [results['email'], 'good', ' ', ' ']
					table.append(row)
				html.table(table)

			html.footer('<a href="https://haveibeenpwned.com/">`;--</a> &nbsp &nbsp &nbsp &nbsp &nbsp <a href="https://github.com/walchko/pwnserver"><i class="fl-github"></i></a>')

			self.wfile.write(str(html))
			return

		# elif self.path.find('/json') > 0:
		# 	print('looking for json!')

		else:
			print 'error', self.path
			self.send_response(404)
			self.send_header('Content-type', 'text/html')
			self.end_headers()

			html = HTML()
			html.h1('Error: {} not found'.format(self.path))
			self.wfile.write(str(html))
			return


def handleArgs():
	parser = argparse.ArgumentParser(description='A simple web sever that checks to see if your accounts have been compromised')
	parser.add_argument('-p', '--port', help='port, default is 9000', type=int, default=9090)
	parser.add_argument('-e', '--emails', help='json list of emails to check', default='emails.json')

	args = vars(parser.parse_args())
	return args


def main():
	args = handleArgs()

	t = PwmThread(args['emails'])
	t.setDaemon(True)
	t.start()

	try:
		server = HTTPServer((gethostname(), args['port']), ServerHandler)
		print "server started"
		server.serve_forever()

	except KeyboardInterrupt:
		print 'main interrupt'
		server.socket.close()


if __name__ == '__main__':
	main()
