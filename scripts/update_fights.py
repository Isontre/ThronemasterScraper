from thronescraper.misc import last_number
from bs4 import BeautifulSoup
from thronescraper import get_numbers
from thronescraper.GetFights import Get_Fights


numbers = get_numbers()
	
last = last_number('Fights/Fights.txt')


for number in numbers:
	if(int(number)<=last):
		continue
	try:
		with open('htmls/'+number+'.html') as f:
			html = f.read()
	except:
		break
	
	print( '-----------------------------------------------------')
	print( number,"/",numbers[-1])
	soup = BeautifulSoup(html,"html.parser")
	#print( Get_Fights(soup))
	
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
