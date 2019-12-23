import web_search, urllib.parse, pdb

def test_duck_duck_go_naruto():
    links = web_search.find_use_duck_duck_go("naruto+ru")
    print("\n".join(links))

def test_duck_duck_go_naruto_russian():
    links = web_search.find_use_duck_duck_go(u"Наруто+Боруто")
    print("\n".join(links))

def test_yahoo_no_js_naruto():
    links = web_search.find_use_yahoo_no_js("naruto+ru")
    print("\n".join(links))

def test_yahoo_no_js_naruto_russian():
    links = web_search.find_use_yahoo_no_js(u"Наруто+Боруто")
    print("\n".join(links))

def test_search_kamisama_anime_english():
    links = web_search.search(u"Kamisama Hajimemashita")
    print("\n".join(links))

def test_search_kamisama_anime_japanise():
    links = web_search.search(u"神様はじめました")
    print("\n".join(links))

if __name__ == "__main__":
    print(u'\nFIND duck_duck_go: u"naruto+ru"')
    test_duck_duck_go_naruto()
    print(u'\nFIND duck_duck_go: u"Наруто+Боруто"')
    test_duck_duck_go_naruto_russian()
    print(u'\nFIND yahho: u"naruto+ru"')
    test_yahoo_no_js_naruto()
    print(u'\nFIND yahho: u"Наруто+Боруто"')
    test_yahoo_no_js_naruto_russian()
    print(u'\nFIND:u"Kamisama Hajimemashita"')
    test_search_kamisama_anime_english()
    print(u'\nFIND:u"神様はじめました"')
    test_search_kamisama_anime_japanise()
