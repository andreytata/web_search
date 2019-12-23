import web_search, urllib.parse

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
    test_duck_duck_go_naruto()
    test_duck_duck_go_naruto_russian()
    test_yahoo_no_js_naruto()
    test_yahoo_no_js_naruto_russian()
    print(u"FIND: KAMISAMA")
    test_search_kamisama_anime_english()
    print(u"FIND: 神様はじめました")
    test_search_kamisama_anime_japanise()
