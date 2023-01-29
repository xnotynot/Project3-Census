# import http.server # Our http server handler for http requests
# import socketserver # Establish the TCP Socket connections
 
# PORT = 8000
 
# class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
#     def do_GET(self):
#         self.path = './index.html'
#         return http.server.SimpleHTTPRequestHandler.do_GET(self)
 
# Handler = MyHttpRequestHandler
 
# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("Http Server Serving at port", PORT)
#     httpd.serve_forever()

from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys
import pymongo
from config import Config

PORT = 8000

client = pymongo.MongoClient(Config.getValue('MongoServer'))
db = client["CensusData"]

class MyHttpRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = '/index.html'
        return SimpleHTTPRequestHandler.do_GET(self)
        # self.send_response(200)
        # # self.send_header("Content-Type", )
        # self.end_headers()
        # # self.wfile.write(content.encode("ascii"))

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super(MyHttpRequestHandler, self).end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

host = sys.argv[1] if len(sys.argv) > 2 else '0.0.0.0'
print("Listening on {}:{}".format(host, PORT))
httpd = HTTPServer((host, PORT),MyHttpRequestHandler)
httpd.serve_forever()