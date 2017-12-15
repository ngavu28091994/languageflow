import webbrowser
import os
import shutil
from os.path import dirname, join


class Board:
    """
    Visualize analyzed results
    """
    def __init__(self, log_folder):
        self.log_folder = log_folder
        """

        Parameters
        ----------
        log_folder: string
            path to log folder
        """

        # Empty log folder
        try:
            shutil.rmtree(log_folder)
        except:
            pass
        finally:
            os.mkdir(log_folder)

        # Copy web source
        source_web_folder = join(dirname(__file__), "board", "web")
        web_folder = join(log_folder, "web")
        shutil.copytree(source_web_folder, web_folder)
        index_file = join(dirname(__file__), "board", "index.html")
        shutil.copy(index_file, join(log_folder, "index.html"))

    def serve(self):
        """ Start LanguageBoard web application
        """

        from http.server import HTTPServer, CGIHTTPRequestHandler
        port = 62000
        os.chdir(self.log_folder)

        httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
        print("Starting LanguageBoard on port: " + str(httpd.server_port))
        webbrowser.open('http://0.0.0.0:{}'.format(port))
        httpd.serve_forever()

