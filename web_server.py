from http.server import HTTPServer, CGIHTTPRequestHandler

import os

cgi_dir = os.path.normpath(os.path.abspath(os.getcwd()))  #.replace("\\","/")
cgi_dir = os.path.join(cgi_dir,"cgi-bin")

class RequestHandler(CGIHTTPRequestHandler):
    def translate_path(self, path):
        """For paths starting with /cgi-bin/, serve from cgi_dir"""
        print(path)
        elts = path.split('/')
        if len(elts)>1 and elts[0]=='' and elts[1]=='cgi-bin':
            translated = os.path.join(cgi_dir,*elts[2:])
            print(translated)
            if not translated.endswith(".py"):
                translated+=".py"
                print("USES:", translated )
            return translated
        return CGIHTTPRequestHandler.translate_path(self, path)    

PORT = 8000

httpd = HTTPServer(("", PORT), RequestHandler)
print("serving at port", PORT)
httpd.serve_forever()
