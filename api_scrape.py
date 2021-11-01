from bs4 import BeautifulSoup
import urllib.request


urls = open('appIDs.txt', 'r')

with urls as f:
    url = f.readline()
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    print(respData)


# soup = BeautifulSoup(, 'html.parser')
# to read html file, webUrl.read()
# Filter by co-op