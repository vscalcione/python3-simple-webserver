from http.server import HTTPServer, BaseHTTPRequestHandler
from getkey import getkey
from sys import exit

class Server(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/':
			self.path = '/index.html'
		try:
			file_to_open = open(self.path[1:]).read()
			self.send_response(200)
		except:
			file_to_open = "Error 404: File Not Found"
		self.send_response(404)
		self.end_headers()
		self.wfile.write(bytes(file_to_open, 'utf-8'))

http_server = HTTPServer(('localhost', 8080), Server)
http_server.serve_forever()
