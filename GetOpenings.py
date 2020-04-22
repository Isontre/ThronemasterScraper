from PySide import QtCore, QtGui, QtWebKit
import sys
from bs4 import BeautifulSoup
import re
import os.path


def Get_Opening(soup,House):

	if House=="Stark":
		S_WF=soup.find("div", {"id": "Order1"}).get('class')[1] if soup.find("div", {"id": "Order1"}).get('class') else 'none'
		S_SS=soup.find("div", {"id": "Order49"}).get('class')[1] if soup.find("div", {"id": "Order49"}).get('class') else 'none'
		S_WH=soup.find("div", {"id": "Order4"}).get('class')[1] if soup.find("div", {"id": "Order4"}).get('class') else 'none'
		return [["Winterfell",S_WF],["White Harbor",S_WH],["Shivering Sea",S_SS]]
		
	elif House=="Greyjoy":
		G_IB=soup.find("div", {"id": "Order40"}).get('class')[1] if soup.find("div", {"id": "Order40"}).get('class') else 'none'
		G_PK=soup.find("div", {"id": "Order12"}).get('class')[1] if soup.find("div", {"id": "Order12"}).get('class') else 'none'
		G_PKP=soup.find("div", {"id": "Order51"}).get('class')[1] if soup.find("div", {"id": "Order51"}).get('class') else 'none'
		G_GW=soup.find("div", {"id": "Order7"}).get('class')[1] if soup.find("div", {"id": "Order7"}).get('class') else 'none'
		return [["Pyke",G_PK],["Greywater Watch",G_GW],["Ironmans Bay",G_IB],["Pyke Port",G_PKP]]
		
	elif House=="Martell":
		M_SD=soup.find("div", {"id": "Order45"}).get('class')[1] if soup.find("div", {"id": "Order45"}).get('class') else 'none'
		M_SH=soup.find("div", {"id": "Order37"}).get('class')[1] if soup.find("div", {"id": "Order37"}).get('class') else 'none'
		M_SS=soup.find("div", {"id": "Order34"}).get('class')[1] if soup.find("div", {"id": "Order34"}).get('class') else 'none'
		return [["Sunspear",M_SS],["Salt Shore",M_SH],["Sea of Dorne",M_SD]]
		
	elif House=="Tyrell":
		T_HG=soup.find("div", {"id": "Order27"}).get('class')[1] if soup.find("div", {"id": "Order27"}).get('class') else 'none'
		T_DM=soup.find("div", {"id": "Order29"}).get('class')[1] if soup.find("div", {"id": "Order29"}).get('class') else 'none'
		T_RS=soup.find("div", {"id": "Order43"}).get('class')[1] if soup.find("div", {"id": "Order43"}).get('class') else 'none'
		return [["Highgarden",T_HG],["Dornish Marches",T_DM],["Redwine Straights",T_RS]]
		
	elif House=="Baratheon":
		B_KW=soup.find("div", {"id": "Order24"}).get('class')[1] if soup.find("div", {"id": "Order24"}).get('class') else 'none'
		B_DS=soup.find("div", {"id": "Order20"}).get('class')[1] if soup.find("div", {"id": "Order20"}).get('class') else 'none'
		B_SB=soup.find("div", {"id": "Order46"}).get('class')[1] if soup.find("div", {"id": "Order46"}).get('class') else 'none'
		return [["Dragonstone",B_DS],["Kingswood",B_KW],["Shipbreaker Bay",B_SB]]
		
	elif House=="Lannister":
		L_GS=soup.find("div", {"id": "Order41"}).get('class')[1] if soup.find("div", {"id": "Order41"}).get('class') else 'none'
		L_LA=soup.find("div", {"id": "Order16"}).get('class')[1] if soup.find("div", {"id": "Order16"}).get('class') else 'none'
		L_SS=soup.find("div", {"id": "Order18"}).get('class')[1] if soup.find("div", {"id": "Order18"}).get('class') else 'none'
		return [["Lannisport",L_LA],["Stoney Sept",L_SS],["Golden Sound",L_GS]]
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
	with open('Openings/OpeningStark.txt', 'r') as the_file:
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
	url="http://game.thronemaster.net/?game="+str(number)+"&review=1"
	print '-----------------------------------------------------'
	print number,"/",numbers[-1]
	html = loadPage(url)
	soup = BeautifulSoup(html,"html.parser")
	GJ=Get_Opening(soup,"Greyjoy")
	TY=Get_Opening(soup,"Tyrell")
	MA=Get_Opening(soup,"Martell")
	LA=Get_Opening(soup,"Lannister")
	BA=Get_Opening(soup,"Baratheon")
	ST=Get_Opening(soup,"Stark")
	
	with open('Openings/OpeningStark.txt', 'a') as the_file:
		the_file.write('%s,%s,%s,%s\n'%(number,ST[0][1],ST[1][1],ST[2][1]))
		
	with open('Openings/OpeningTyrell.txt', 'a') as the_file:
		the_file.write('%s,%s,%s,%s\n'%(number,TY[0][1],TY[1][1],TY[2][1]))	

	with open('Openings/OpeningBaratheon.txt', 'a') as the_file:
		the_file.write('%s,%s,%s,%s\n'%(number,BA[0][1],BA[1][1],BA[2][1]))			

	with open('Openings/OpeningLannister.txt', 'a') as the_file:
		the_file.write('%s,%s,%s,%s\n'%(number,LA[0][1],LA[1][1],LA[2][1]))
	try:
		with open('Openings/OpeningGJ.txt', 'a') as the_file:
			the_file.write('%s,%s,%s,%s,%s\n'%(number,GJ[0][1],GJ[1][1],GJ[2][1],GJ[3][1]))
	except: 
		with open('Openings/OpeningGJ.txt', 'a') as the_file:
			the_file.write('%s,%s,%s,%s\n'%(number,GJ[0][1],GJ[1][1],GJ[2][1]))
	
	with open('Openings/OpeningMartell.txt', 'a') as the_file:
		the_file.write('%s,%s,%s,%s\n'%(number,MA[0][1],MA[1][1],MA[2][1]))

app.exit()