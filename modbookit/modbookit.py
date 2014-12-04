import socket
import urllib2
import json

URL = "http://it-ebooks-api.info/v1/"
URL_SEARCH = "search/%s"
URL_PAGE = "search/%s/page/%s"
URL_DETAIL = "book/%s"


# checking connection
def checkConnection():
    REMOTE_SERVER = 'www.google.com'
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

def getSearchJson(query):
    query = query.replace(" ","%20")
    url = URL + URL_SEARCH % (query)
    respone = urllib2.urlopen(url)
    jsonData = json.load(respone)
    return jsonData

def getPageJson(query, page):
    q = query.replace(" ","%20")
    url = URL + URL_PAGE % (q, str(page))
    respone = urllib2.urlopen(url)
    jsonData = json.load(respone)
    return jsonData

def getBookDetailJson(ids):
    ids = str(ids).replace(" ","")
    url = URL + URL_DETAIL % ids
    respone = urllib2.urlopen(url)
    jsonData = json.load(respone)
    return jsonData


#print checkConnection()

#print getSearchJson("Php MySQL")
#print getPageJson("Python For Kids", "9")
#print getBookDetailJson(str(2279690981))