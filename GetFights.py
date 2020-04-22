from PySide import QtCore, QtGui, QtWebKit
import sys
from bs4 import BeautifulSoup
import re
import os

def Get_Fights(soup):

	list=[]
	for elem in soup(text=re.compile(r'\[Attack\]')):
		
		#print elem.parent
		#roundnumber=elem.parent.parent.parent.findChildren('th')[0].text
		#print roundnumber
		
		
			
		
		text=elem.parent.text
		try:
			list.append(re.search(r"([a-zA-Z]+) is attacking ([a-zA-Z]+) in ([a-zA-Z' ]+) from ([a-zA-Z' ]+) wit",text).groups())
		except:
			print "Exception Raised",text
			list.append(re.search(r"([a-zA-Z]+) is attacking ([a-zA-Z]+) in ([a-zA-Z' ]+) from ([a-zA-Z']+)",text).groups())
	

	return list

	


filename="6pgames"	

with open(filename+'.txt') as f:
	lines = f.read().splitlines()

numbers=[]
for line in lines:
	numbers.append(line.split(',', 1)[0])	
	
	
try:
	with open('Fights/Fights.txt', 'r') as the_file:
		for line in the_file:
			pass
		last = int(line.split(',', 1)[0])
		print "Last Number:",last
except:
	last=0
	print"No file found"
	
	
	
	

for number in numbers:
	if(int(number)<=last):
		continue
	try:
		with open('htmls/'+number+'.html') as f:
			html = f.read()
	except:
		break
	
	print '-----------------------------------------------------'
	print number,"/",numbers[-1]
	soup = BeautifulSoup(html,"html.parser")
	#print Get_Fights(soup)
	
	#GJ=Get_Fights(soup,"Greyjoy")
	#TY=Get_Fights(soup,"Tyrell")
	#MA=Get_Fights(soup,"Martell")
	#LA=Get_Fights(soup,"Lannister")
	#BA=Get_Fights(soup,"Baratheon")

	
		
	
	with open('Fights/Fights.txt', 'a') as the_file:
		for fight in Get_Fights(soup):
			the_file.write('%s,%s,%s,%s,%s\n'%(number,fight[0],fight[1],fight[2],fight[3]))
		
	#with open('Fights/FightsTyrell.txt', 'a') as the_file:
	#	the_file.write('%s,%s,%s\n'%(number,TY[0],TY[1]))

	#with open('Fights/FightsBaratheon.txt', 'a') as the_file:
	#	the_file.write('%s,%s,%s\n'%(number,BA[0],BA[1]))			

	#with open('Fights/FightsLannister.txt', 'a') as the_file:
	#	the_file.write('%s,%s,%s\n'%(number,LA[0],LA[1]))
		
	#with open('Fights/FightsGJ.txt', 'a') as the_file:
	#	the_file.write('%s,%s,%s\n'%(number,GJ[0],GJ[1]))
	
	#with open('Fights/FightsMartell.txt', 'a') as the_file:
	#	the_file.write('%s,%s,%s\n'%(number,MA[0],MA[1]))
