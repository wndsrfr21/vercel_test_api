from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib import parse

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    s = self.path
    dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
            if "name" in dic:
            message = "Hello, " + dic["name"] + "!"
        else:
            message = "Hello, stranger!"
    self.wfile.write(message.encode())
    return
