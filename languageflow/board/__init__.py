"""
Visualize analyzed results
"""
import webbrowser
import os
import shutil
from os.path import dirname, join


def init_board(folder):
    """

    Parameters
    ----------
    folder: string
        log folder
    """
    web_folder = join(folder, "web")
    try:
        shutil.rmtree(web_folder)
    except:
        pass
    source_web_folder = join(dirname(__file__), "board", "web")
    shutil.copytree(source_web_folder, web_folder)
    index_file = join(dirname(__file__), "board", "index.html")
    shutil.copy(index_file, join(folder, "index.html"))

def board(folder):
    """ Auto detect type from log data and start LanguageBoard

    Parameters
    ----------
    folder: string
        log folder
    """

    from http.server import HTTPServer, CGIHTTPRequestHandler
    port = 62000
    init_board(folder)
    os.chdir(folder)

    httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
    print("Starting LanguageBoard on port: " + str(httpd.server_port))
    webbrowser.open('http://localhost:{}'.format(port))
    httpd.serve_forever()
