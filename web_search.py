#/usr/bin/python3

""" Serch Web use "Duck-Duck-Go" serch engine
>>> import web_search
>>> urls = web_search.find_use_duck_duck_go("anime+ru"))
python3 -m web_search naruto boruto online ru 
"""

import re, urllib.request, urllib.parse, bs4, sys, pdb

black_list=\
{ u"https://smotret-anime.online" : u"платный"
#, u"https://google.com"           : u"повторный поиск, - эхо ключевых слов запроса"
#, u"https://animego"              : u"тест черного списка"
}

def find_use_duck_duck_go( query ):
    """  Serch Web use "Duck-Duck-Go" serch engine.
       Return sorted urls list w/o dublicates
    """
    query = "https://duckduckgo.com/html/?q=%s" % query
    buff  = str(urllib.request.urlopen(query).read())
    bs    = bs4.BeautifulSoup( buff, "lxml" )
    links = [ re.findall( "uddg=(.*)\" rel", str(i) ) for i in bs.find_all('a') if "uddg=" in repr(i) ]
    links = [ urllib.parse.unquote( i[0] ) for i in links if i ]
    links = [ i.replace("https://www.", "https://") for i in links ]
    links = [ i.replace("http://www.", "http://") for i in links ]
    clean = [ ]
    for key in black_list:
        for link in links:
            if link.startswith(key):
                print ("REMOVE " + key + "=>" + black_list[key] )
                continue
            clean.append(link)
    return sorted( [ i for i in set(clean) ] )

if __name__=="__main__":
    print(sys.prefix)
    print(sys.version)
    query = "%2B".join( [ urllib.parse.quote(i) for i in sys.argv[1:] ] )
    print( "\n".join( [ "%02d %s" % i for i in enumerate( find_use_duck_duck_go( query ) ) ] ) )
