from PySide import QtCore, QtGui, QtWebKit
import sys
from bs4 import BeautifulSoup


def Get_Castles(soup,House):

	if House=="Stark":
		S_SH=soup.find("div", {"id": "StrongholdS"}).text
		S_CA=soup.find("div", {"id": "CityS"}).text
		return [S_SH,S_CA]
		
	elif House=="Greyjoy":
		S_SH=soup.find("div", {"id": "StrongholdG"}).text
		S_CA=soup.find("div", {"id": "CityG"}).text
		return [S_SH,S_CA]
		
	elif House=="Martell":
		S_SH=soup.find("div", {"id": "StrongholdM"}).text
		S_CA=soup.find("div", {"id": "CityM"}).text
		return [S_SH,S_CA]
		
	elif House=="Tyrell":
		S_SH=soup.find("div", {"id": "StrongholdT"}).text
		S_CA=soup.find("div", {"id": "CityT"}).text
		return [S_SH,S_CA]
		
	elif House=="Baratheon":
		S_SH=soup.find("div", {"id": "StrongholdB"}).text
		S_CA=soup.find("div", {"id": "CityB"}).text
		return [S_SH,S_CA]
		
	elif House=="Lannister":
		S_SH=soup.find("div", {"id": "StrongholdL"}).text
		S_CA=soup.find("div", {"id": "CityL"}).text
		return [S_SH,S_CA]
	else:
		print "Error, House not found"
		return 0
	




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
	with open('Castles/CastlesStark.txt', 'r') as the_file:
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
	GJ=Get_Castles(soup,"Greyjoy")
	TY=Get_Castles(soup,"Tyrell")
	MA=Get_Castles(soup,"Martell")
	LA=Get_Castles(soup,"Lannister")
	BA=Get_Castles(soup,"Baratheon")
	ST=Get_Castles(soup,"Stark")
	
	with open('Castles/CastlesStark.txt', 'a') as the_file:
		the_file.write('%s,%s,%s\n'%(number,ST[0],ST[1]))
		
	with open('Castles/CastlesTyrell.txt', 'a') as the_file:
		the_file.write('%s,%s,%s\n'%(number,TY[0],TY[1]))

	with open('Castles/CastlesBaratheon.txt', 'a') as the_file:
		the_file.write('%s,%s,%s\n'%(number,BA[0],BA[1]))			

	with open('Castles/CastlesLannister.txt', 'a') as the_file:
		the_file.write('%s,%s,%s\n'%(number,LA[0],LA[1]))
		
	with open('Castles/CastlesGJ.txt', 'a') as the_file:
		the_file.write('%s,%s,%s\n'%(number,GJ[0],GJ[1]))
	
	with open('Castles/CastlesMartell.txt', 'a') as the_file:
		the_file.write('%s,%s,%s\n'%(number,MA[0],MA[1]))

app.exit()