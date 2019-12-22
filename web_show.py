import os, sys, io, tempfile, webbrowser;

from web_search import search                                         # import our module with web search function

if not tempfile.tempdir: tempfile.mktemp()                            # is init 'tempdir' variable

def main(query):
    out_path=os.path.join(tempfile.tempdir, "out_file.html")          # create output file path
    out_path=os.path.normpath(out_path).replace('\\', '/')            # path separators to *nix separators   
    body = u"<h1>" + sys.version + " at " + sys.prefix + "</h1>\n"    # create page-body unicode string, add python info
    body += u'<p>' + query + "</p>\n"  # add query line, 
    body +="\n".join( [ u'<a href="%s">[%s]</a><br>' % (i,i) for i in search(query) ] ) # add query search results
    web_page=io.open("web_show.html", encoding = 'utf8').read()  # open and read html-page tempate
    web_page=web_page.replace(u"%%get_body%%", body)
    out_file=io.open(out_path, 'w', encoding='utf8')
    out_file.write(web_page)
    out_file.close()
    webbrowser.open("file://" + out_path)                     # show out file use web browswer

if __name__=='__main__':
    query = "+".join(sys.argv[1:])
    if not query:
        sys.exit(0)
    main( query )
