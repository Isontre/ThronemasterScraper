from PySide import QtCore, QtGui, QtWebKit
import sys
from bs4 import BeautifulSoup

def loadPage(url):
	page = QtWebKit.QWebPage()
	loop = QtCore.QEventLoop() # Create event loop
	page.mainFrame().loadFinished.connect(loop.quit) # Connect loadFinished to loop quit
	page.mainFrame().load(url)
	loop.exec_() # Run event loop, it will end on loadFinished
	return page.mainFrame().toHtml()
		
	


		
filename="6pgames"	

with open(filename+'.txt') as f:
	lines = f.read().splitlines()

numbers=[]
for line in lines:
	numbers.append(line.split(',', 1)[0])	
	
	
try:
	with open('winners.txt', 'r') as the_file:
		for line in the_file:
			pass
		last = int(line.split(',', 1)[0])
		print "Last Number:",last
except:
	last=0
	print"No file found"

	
	
app = QtGui.QApplication(sys.argv)

for number in numbers:
	if(int(number)<=last):
		continue
	url="http://game.thronemaster.net/?game="+str(number)
	print '-----------------------------------------------------'
	print number,"/",numbers[-1]
	html = loadPage(url)
	soup = BeautifulSoup(html,"html.parser")
	winner=soup.find("div", {"id": "gameStateText"}).find('b').text.split(' ', 1)[0]
	print winner
	
	with open('winners.txt', 'a') as the_file:
		the_file.write('%s,%s\n'%(number,winner))

app.exit()