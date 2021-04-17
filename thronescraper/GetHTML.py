from PySide import QtCore, QtGui, QtWebKit
import sys
from bs4 import BeautifulSoup
import os.path


def loadPage(url):
	page = QtWebKit.QWebPage()
	loop = QtCore.QEventLoop() # Create event loop
	page.mainFrame().loadFinished.connect(loop.quit) # Connect loadFinished to loop quit
	page.mainFrame().load(url)
	loop.exec_() # Run event loop, it will end on loadFinished
	return page.mainFrame().toHtml()
	
def Winner(soup):
	return soup('table')[1].findAll('tr')[-2].findAll('td')[2].text.split(' ', 1)[0]

def Settings(soup):

	try:
		if(soup('table')[1].findAll('tr')[7].findAll('th')[1].string!="PLANNING"):
			return 0
	except:
		print "No 6 players"
		return 0
	
	#check if game is over:
	if(soup('table')[1].findAll('tr')[-2].findAll('td')[2].text.split(' ', 1)[1]!="wins this game of thrones!"):
		print "The game seems not to be over"
		return 0
	
	
	lala=[]
	for row in soup.findAll('table')[2].findAll('tr'):
		try:
			list=row.findAll('td')[1].text
			lala.append(list)
		except:
			continue
	
	#Give 0 if ToB:
	if(lala[8]=="YES"):
		print "ToB"
		return 0
	elif(lala[8]=="NO"):
		print "No ToB"
	else:
		print "Some Error occured"
		return 0

	#2nd Edition HouseCards	
	if(lala[3]=="NO"):
		print "1st Edition House Cards"
		return 0
	elif(lala[3]=="YES"):
		print "2nd Edition House Cards"
	else:
		print "Some Error occured"
		return 0
		
	
	return 1

def is_rated(soup):
	if(soup.findAll('table')[3].find('tr').text.split(' ', 1)[0]!="\nRATED"):
		print "Unrated game"
		return "unrated"
	else:
		return "rated"

def get_Date(soup):
	return str(soup('table')[1].findAll('tr')[-2].findAll('td')[3].text.split(',', 1)[0])



filename="6pgames"	

with open(filename+'.txt') as f:
	lines = f.read().splitlines()

numbers=[]
for line in lines:
	numbers.append(line.split(',', 1)[0])
	
app = QtGui.QApplication(sys.argv)	

	

for number in numbers:
	if os.path.isfile("htmls/"+str(number)+".html"):
		continue


	url="http://game.thronemaster.net/?game="+str(number)+"&show=log"
	print '-----------------------------------------------------'
	print number,"/",numbers[-1]
	html = loadPage(url).encode('utf-8')
	with open("htmls/"+str(number)+".html", 'w') as the_file:
		the_file.write(html)

app.exit()




