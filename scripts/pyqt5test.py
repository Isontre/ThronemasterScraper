from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEnginePage,QWebEngineView
from bs4 import BeautifulSoup
import sys, signal

class Browser(QWebEngineView):
    def __init__(self):
        QWebEngineView.__init__(self)
        self.loadProgress.connect(self._progress)
        self.loadFinished.connect(self._loadFinished)
        self.frame = self.page()

    def _progress(self, progress):
        print(str(progress) + "%")

    def _loadFinished(self):
        print("Load Finished")
        html = self.frame.toHtml(self.callback).encode('utf-8')
        self.soup = BeautifulSoup(html)
        #print soup.prettify()
        self.close()

    def callback(self, html):
        print(str(html).encode('utf-8'))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    br = Browser()
    url = QUrl("http://game.thronemaster.net/?game=90001")
    br.load(url)
    br.show()
    if signal.signal(signal.SIGINT, signal.SIG_DFL):
        sys.exit(app.exec_())
    app.exec_()