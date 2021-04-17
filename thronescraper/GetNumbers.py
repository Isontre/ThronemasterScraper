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
end=150000

try:
	with open(filename+'.txt', 'r') as the_file:
		for line in the_file:
			pass
		last = int(line.split(',', 1)[0])
		print "Last Number:",last
except:
	last=0
	print"No file found"



app = QtGui.QApplication(sys.argv)	

for number in range(last+1,end):
	url="http://game.thronemaster.net/?game="+str(number)+"&show=log"
	print '-----------------------------------------------------'
	print number
	html = loadPage(url)
	print "..html loaded"
	soup = BeautifulSoup(html,"html.parser")
	if(Settings(soup)):
		print "Right Settings"			
		row=str(number)+","+Winner(soup)+","+get_Date(soup)+","+is_rated(soup)
		with open(filename+".txt", "a") as f:
			f.write("%s\n" % row)
	else:
		print "Not the right settings"

app.exit()




