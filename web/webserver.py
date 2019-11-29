"""
Implement an HTTP web server in Python that knows how to run server-side CGI scripts
coded in Python;
serves files and scripts from current working dir;
Python scripts must be stored in webdir/cgi-bin or webdir/htbin;
"""

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port = 80 # default http://localhost/, else use http://localhost:xxxx/

os.chdir(webdir)
server_address = ("", port)
server_obj = HTTPServer(server_address, CGIHTTPRequestHandler)
server_obj.serve_forever()

