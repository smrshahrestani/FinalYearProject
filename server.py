

import SimpleHTTPServer
import SocketServer

# from flask import Flask, render_template, request

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
file = codecs.open("index.py", "r", "utf-8")
print(file.read())

# app = Flask(__name__)
# @app.route("/", methods=["POST"])
# def getValue():
#     print request.form['name']
#     return render_template('index.py')