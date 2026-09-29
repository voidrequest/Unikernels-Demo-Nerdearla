from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        mensaje = "<h1>Una pequeña demo de Server Python en Unikernels!</h1>"
        self.wfile.write(mensaje.encode('utf-8'))

print("Escuchando en el puerto 9000...")
HTTPServer(('', 9000), SimpleHandler).serve_forever()
