""" Serch Web use "Duck-Duck-Go" serch engine
>>> import web_search
>>> urls = web_search.search("anime+ru"))
python3 -m web_search naruto boruto online ru 
"""

import re, urllib.request, urllib.parse, bs4, sys, pdb

black_list=\
{ u"https://smotret-anime.online" : u"платный"
, u"https://google.com"           : u"повторный поиск, - эхо ключевых слов запроса"
#, u"https://animego"              : u"тест черного списка"
}

def find_use_bing_no_js(query):
    """Search Web use "bing". Return sorted urls list w/o dublicates"""
    query = urllib.parse.quote(query)  # comment this line to crash test 2 in unittests 
    query = "http://www.bing.com/search?q=%s" % query
    buff  = str(urllib.request.urlopen(query).read())
    bs    = bs4.BeautifulSoup( buff, "html.parser" )
    links = [ i for i in bs.find_all('a') if not ".microsoft." in repr(i) ]
    links = [ re.findall("href=\"(http[^\"]*)\"", str(i)) for i in links ]
    links = [ urllib.parse.unquote( i[0] ) for i in links if i ]
    links = [ i.replace("https://www.", "https://") for i in links ]
    links = [ i.replace("http://www.", "http://") for i in links ]
    return sorted(set(links))

def find_use_yahoo_no_js( query ):
    """Serch Web use "Yahoo". Return sorted urls list w/o dublicates"""
    query = urllib.parse.quote(query)  # comment this line to crash test 2 in unittests 
    query = "https://search.yahoo.com/search?p=%s&ei=UTF-8&nojs=1" % query
    buff  = str(urllib.request.urlopen(query).read())
    bs    = bs4.BeautifulSoup( buff, "html.parser" )
    links = [ i for i in bs.find_all('a') if not ".yahoo.com" in repr(i) ]
    links = [ re.findall("href=\"([^\"]*)\"", str(i)) for i in links ]
    links = [ urllib.parse.unquote( i[0] ) for i in links if i ]
    links = [ i.replace("https://www.", "https://") for i in links ]
    links = [ i.replace("http://www.", "http://") for i in links ]
    return sorted(set(links))

def find_use_duck_duck_go( query ):
    """Serch Web use "Duck-Duck-Go". Return sorted urls list w/o dublicates"""
    query = urllib.parse.quote(query)  # comment this line to crash test 2 in unittests 
    query = "https://duckduckgo.com/html/?q=%s" % query
    buff  = str(urllib.request.urlopen(query).read())
    bs    = bs4.BeautifulSoup( buff, "html.parser" )
    links = [ re.findall( "uddg=(.*)\" rel", str(i) ) for i in bs.find_all('a') if "uddg=" in repr(i) ]
    links = [ urllib.parse.unquote( i[0] ) for i in links if i ]
    links = [ i.replace("https://www.", "https://") for i in links ]
    links = [ i.replace("http://www.", "http://") for i in links ]
    return sorted(set(links))

def search(query):
    yahoo_result = find_use_yahoo_no_js  ( query )
    duck_duck_go = find_use_duck_duck_go ( query )
    bing_results = find_use_bing_no_js   ( query )
    links = yahoo_result + duck_duck_go + bing_results
    clean = [ ]
    for key in black_list:
        for link in links:
            if not link.startswith("http"):
                print ("REMOVE " + link + "=> AS INVALID LINK" )
                continue
            if link.startswith(key):
                print ("REMOVE " + key + "=>" + black_list[key] )
                continue
            clean.append(link)
    return sorted( set( clean ) )

if __name__=="__main__":
    query = "+".join( sys.argv[1:] )
    if "" == query:
        sys.exit(0)
    result = search( query )
    print( sys.prefix, sys.version )
    print( '''Web Search "%s"''' % query )
    print( "\n".join( [ "%02d %s" % i for i in enumerate( result ) ] ) )

    #print("\n".join([ re.findall(r"""<a.+href=\"([^>]*)\">""",str(i))[0] for i in buff.find_all('a') ]))
