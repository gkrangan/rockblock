# Python HTTP Webserver to receive POST messages from Rock7 Servers

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

def hex_to_text(hex_string):
    """Converts a hexadecimal string to text."""

    # Remove the leading '0x' if present
    if hex_string.startswith("0x"):
        hex_string = hex_string[2:]

    # Convert the hex string to bytes
    bytes_object = bytes.fromhex(hex_string)

    # Decode the bytes object to text (assuming ASCII encoding)
    text = bytes_object.decode("utf-8")

    return text

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Process the POST data here
        print("Received POST data:", post_data)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"POST request received")

        # Process the received message
        decoded_post_data = post_data.decode('utf-8')
        # print(str(decoded_post_data).split('&'))
        output = str(decoded_post_data).split('&')
        print(output)
       
        print(output[0].split('='))
        print(output[1].split('='))
        print(output[2].split('='))
        print(output[3].split('='))
        print(output[4].split('='))
        print(output[5].split('='))
        print(output[6].split('='))
        print(output[7].split('='))
        print(output[8].split('='))
        print(output[9].split('='))
     
        # Extract message in Hex:
        # hex_string = output[9].split('=')[1].rstrip("'")
        hex_string = output[9].split('=')[1]
        print("Message Received in Hex:" + hex_string)
        text = hex_to_text(hex_string)
        print("Message Received ASCII: " + text)

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Starting Python HTTP Webserver to receive POST messages from Rock7 Servers on port 8000...")
    httpd.serve_forever()
