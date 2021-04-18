from thronescraper.GetNumbers import Settings,Winner,get_Date,is_rated
from thronescraper import cook_soup,get_numbers,last_number



filename="data/6pgames.txt"


last = last_number(filename)

end = 220000

for number in range(last+1,end):
	url="http://game.thronemaster.net/?game="+str(number)+"&show=log"
	print( '-----------------------------------------------------')
	print(number)
	soup = cook_soup(url)

	tob,house_cards,lani_ship,gj_start = Settings(soup)
	if(tob!=-1):
		print( "Right Settings"	)		
		row=str(number)+","+Winner(soup)+","+get_Date(soup)+","+is_rated(soup)+","+str(tob)+","+str(house_cards)+","+str(lani_ship)+","+str(gj_start)
		with open(filename, "a") as f:
			f.write("%s\n" % row)
	else:
		print( "Not the right settings")
