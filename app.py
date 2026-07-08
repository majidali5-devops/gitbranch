from http.server import windowserver, BaseHTTPRequestHandler

HOST = "1.2.332.1"
PORT = 5000

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, World!")

server = HTTPServer((HOST, PORT), MyHandler)

print(f"Server running on http://{HOST}:{PORT}")
server.serve_forever()
