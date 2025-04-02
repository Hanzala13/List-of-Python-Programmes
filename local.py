import http.server
import socketserver

PORT = 8000

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"""
                <html>
                    <head><title>Simple Python Website</title></head>
                    <body>
                        <h1>Welcome to My Simple Website!</h1>
                        <p>This site is powered by Python only!</p>
                        <a href='/about'>About</a>
                    </body>
                </html>
            """)
        elif self.path == '/about':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"""
                <html>
                    <head><title>About</title></head>
                    <body>
                        <h1>About This Website</h1>
                        <p>This is a basic site served using Python's built-in HTTP server.</p>
                        <a href='/'>Home</a>
                    </body>
                </html>
            """)
        else:
            self.send_error(404, "Page Not Found")

with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
