from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json
from magichome import MagicHomeApi

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        # logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
        #         str(self.path), str(self.headers), post_data.decode('utf-8'))

        [r, g, b] = json.loads(post_data.decode('utf-8'))['RGBcolor']
        print("Red: {} Green: {} Blue: {}".format(r,g,b))
        controller.update_device(r,g,b)
        
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv
    controller = MagicHomeApi(argv[1], 1)
    controller.turn_on()

    if len(argv) == 2:
        run(port=int(argv[2]))
    else:
        run()
