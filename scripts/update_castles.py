"""Updates the castles.txt file in the data folder
"""
from thronescraper.misc import last_number
from thronescraper import cook_soup,get_numbers
from thronescraper.GetCastles import Get_Castles

numbers = get_numbers()

castle_filename = 'Castles/CastlesStark.txt'
last = last_number(castle_filename)

for number in numbers:
	if(int(number)<=last):
		continue
	url="http://game.thronemaster.net/?game="+str(number)
	print( '-----------------------------------------------------')
	print( number,"/",numbers[-1])
	soup = cook_soup(url)
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