import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import QUrl,QEventLoop,QTimer
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEnginePage,QWebEngineView
from time import sleep


def cook_soup(url):
    """Returns a very beautiful soup from an url

    Args:
        url (str): Just a url
    """
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

    req = requests.get(url, headers)
    print("..html loaded")
    return BeautifulSoup(req.content,"html.parser")

def get_html(url):
    """Returns an html from an url

    Args:
        url (str): Just a url
    """
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

    req = requests.get(url, headers)
    print("..html loaded")
    return req.content


def get_numbers():
    """
    Returns game numbers of the 6pgames.txt file
    """
    filename="data/6pgames.txt"	
    with open(filename) as f:
        lines = f.read().splitlines()

    numbers=[]
    for line in lines:
        numbers.append(line.split(',', 1)[0])

    return numbers


def last_number(filename):
    try:
        with open(filename, 'r') as the_file:
            for line in the_file:
                pass
            last = int(line.split(',', 1)[0])
            print( "Last Number:",last)
    except:
        last = 0
        print("No file found")

    return last


def get_html(html_str):
    return html_str

def loadPage(url):
	page = QWebEnginePage()
	loop = QEventLoop() # Create event loop
	page.loadFinished.connect(loop.quit) # Connect loadFinished to loop quit
	page.load(QUrl(url))
	loop.exec_() # Run event loop, it will end on loadFinished
	return page.toHtml(get_html)


class Page(QWebEngineView):
    def __init__(self, url):
        self.app = QApplication([])
        QWebEngineView.__init__(self)
        self.html = ''

    def open(self, url, timeout=60):
        """Wait for download to complete and return result"""
        loop = QEventLoop()
        timer = QTimer()
        #timer.setSingleShot(True)
        timer.timeout.connect(loop.quit)
        self.loadFinished.connect(loop.quit)
        self.load(QUrl(url))
        timer.start(timeout * 1000)
        loop.exec_() # delay here until download finished
        if timer.isActive():
            # downloaded successfully
            timer.stop()
            sleep(0.3)
            self.page().toHtml(self.callable)
        else:
            # timed out
            print ('Request timed out:' + url)
 
        self.app.exec_()
 
    def callable(self, data):
        self.html = data
        self.app.quit()
 
    def get_html(self):
        """Shortcut to return the current HTML"""
        return self.html

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print('Load finished')


def soup_from_html(html):
    """Returns soup

    Args:
        html ([type]): [description]
    """
    return BeautifulSoup(html,"html.parser")