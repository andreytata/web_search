import web_search, urllib.parse

def test_naruto():
    links = web_search.find_use_duck_duck_go("naruto+ru")
    print("\n".join(links))
    #assert func(3) == 4

def test_naruto_russian():
    links = web_search.find_use_duck_duck_go(u"Наруто+Боруто")
    print("\n".join(links))

if __name__ == "__main__":
    test_naruto()
    test_naruto_russian()