import sys

from bs4 import BeautifulSoup
from bs4.dammit import UnicodeDammit

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEnginePage


class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.update_url(url)

    def update_url(self,url):
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print('Load finished')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()





items = [
    "http://stackoverflow.com",
    "http://google.com",
]


def main():
    webpage = Page(items[0])
    for url in items:
        webpage.update_url(url)
        print(webpage.html)



if __name__ == "__main__":
    main()