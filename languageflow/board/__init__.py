"""
Visualize analyzed result
"""

import webbrowser
from http.server import HTTPServer, CGIHTTPRequestHandler
import os


def board(folder):
    """

    Parameters
    ----------
    folder: string
        log folder
    """

    port = 62000

    web_dir = folder
    os.chdir(web_dir)
    httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
    print("Starting LanguageBoard on port: " + str(httpd.server_port))
    webbrowser.open('http://localhost:{}'.format(port))
    httpd.serve_forever()
