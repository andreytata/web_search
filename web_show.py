import os, io, tempfile, webbrowser;

if not tempfile.tempdir: tempfile.mktemp()                # is init 'tempdir' variable

out_path=os.path.join(tempfile.tempdir, "out_file.html")  # create output file path
out_path=os.path.normpath(out_path).replace('\\', '/')    # path separators to *nix separators   

web_page=io.open("web_show.html", encoding = 'utf8').read()

from web_search import search

body = "\n".join( [ u'<a href="%s">[%s]</a><br>' % (i,i) for i in search("Naruto") ] )

web_page=web_page.replace(u"%%get_body%%", body)

out_file=io.open(out_path, 'w', encoding='utf8')
out_file.write(web_page)
out_file.close()

webbrowser.open("file://" + out_path)                     # show out file use web browswer
