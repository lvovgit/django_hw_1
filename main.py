import json
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    json_data = []

    def load_json(self):
        with open('list.json', 'r') as json_file:
            return json.load(json_file)

    def save_json(self, json_data):
        with open('list.json', 'w') as json_file:
            json.dump(json_data, json_file)

    def do_POST(self):

        c_len = int(self.headers.get('Content-Length'))
        body = self.rfile.read(c_len)
        json_body = json.loads(body.decode())
        self.json_data.append(json_body)
        print(self.json_data)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes('[]', "utf-8"))

    def do_GET(self):
        print('Hello, World wide web')
        json_data = self.load_json()
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(json_data), "utf-8"))


if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped")



