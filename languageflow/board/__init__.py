"""
Visualize analyzed results
"""
import json
import webbrowser
import os
import shutil
from os.path import dirname, join


def init_board(type, folder):
    """

    Parameters
    ----------
    type: string
        either 'multiclass', 'multilabel'
    folder: string
        log folder
    """
    source_folder = join(dirname(__file__), type)
    shutil.copy(join(source_folder, "index.html"), join(folder, "index.html"))


def get_type(folder):
    """

    Parameters
    ----------
    folder: string
        log folder

    Returns
    -------
    type: string
        type of problem
    """
    type = json.loads(open(join(folder, "result.json")).read())["type"]
    return type


def board(folder):
    """

    Parameters
    ----------
    folder: string
        log folder
    """

    from http.server import HTTPServer, CGIHTTPRequestHandler
    port = 62000
    type = get_type(folder)
    init_board(type, folder)
    os.chdir(folder)

    httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
    print("Starting LanguageBoard on port: " + str(httpd.server_port))
    webbrowser.open('http://localhost:{}'.format(port))
    httpd.serve_forever()
