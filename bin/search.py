import webbrowser as web

def search(string):
    url = "www.google.com/search?q={}".format(string)
    web.open_new_tab(url = url)
search('superman')
    