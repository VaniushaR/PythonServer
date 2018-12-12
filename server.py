import http.server
import urllib.parse as urlparse
import json
import socketserver
from random import randint

PORT = 8000


def returnHTML(res):
    res.send_response(200)
    res.send_header('Content-type', 'text/html')
    res.end_headers()

    html = open("./index.html").read()
    res.wfile.write(bytes(html, "utf8"))
    return


def returnJSON(res):
    print(res)
    res.send_response(200)
    res.send_header('Content-type', 'application/json')
    res.end_headers()

    message = json.dumps({"type": "json"})
    res.wfile.write(bytes(message, "utf8"))
    return


class Handler(http.server.BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    def do_GET(self):
        parsed = urlparse.urlparse(self.path)
        query = urlparse.parse_qs(parsed.query)
        if(parsed.path == "/"):
            return HTML(self, query)
            return
        if(parsed.path == "/json"):
            return JSON(self, query)
            return


socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Running on port: ", str(PORT))
    httpd.serve_forever()
