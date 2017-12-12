"""
Visualize log results
"""

import webbrowser
import os


def board(folder):
    """

    Parameters
    ----------
    folder: string
        log folder
    """

    from http.server import HTTPServer, CGIHTTPRequestHandler
    port = 62000

    os.chdir(folder)
    httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
    print("Starting LanguageBoard on port: " + str(httpd.server_port))
    webbrowser.open('http://localhost:{}'.format(port))
    httpd.serve_forever()
