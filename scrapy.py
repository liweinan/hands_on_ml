from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html.read(), 'html.parser')
        return bs.body.h1
    except HTTPError as e:
        return None
    except AttributeError as e:
        return None


title = get_title('http://www.pythonscraping.com/pages/page1.html')
if title is None:
    print('Title could not be found')
else:
    print(title)
