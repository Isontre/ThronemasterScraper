from thronescraper import cook_soup



def Winner(soup):
	return soup('table')[1].findAll('tr')[-2].findAll('td')[2].text.split(' ', 1)[0]

def Settings(soup):
	"""
	Returns -1,-1,-1,-1 if it wasn't a 6 player game or anything else went wrong
	Returns tob,2nd_ed_house_cards,lani_ship,gj_start position otherwise. 0=="NO", 1="YES"  
	"""
	try:
		# Checks if the first 6 entries are PLANNING which indicates if 6 players are participating
		if(soup('table')[1].findAll('tr')[7].findAll('th')[1].string!="PLANNING"):
			return -1,-1,-1,-1
	except:
		print( "No 6 players")
		return -1,-1,-1,-1
	
	#check if game is over:
	if(soup('table')[1].findAll('tr')[-2].findAll('td')[2].text.split(' ', 1)[1]!="wins this game of thrones!"):
		print( "The game seems not to be over or was aborted.")
		return -1,-1,-1,-1
	
	
	game_settings=[]
	for row in soup.findAll('table')[2].findAll('tr'):
		try:
			setting = row.findAll('td')[0].text
			value = row.findAll('td')[1].text
			game_settings.append([setting,value])
		except:
			continue
	
	for settings in game_settings:
		if "Tides Of Battle" in settings[0]:
			if(settings[1]=="YES"):
				print( "ToB:","YES")
				tob = 1
			elif(settings[1]=="NO"):
				print( "ToB:","NO")
				tob = 0
			else:
				print( "Some Error occured")
				return -1,-1,-1,-1
		elif "House Cards" in settings[0]:
			if(settings[1]=="YES"):
				print( "House Cards:","YES")
				house_cards = 1
			elif(settings[1]=="NO"):
				print( "House Cards:","NO")
				house_cards = 0
			else:
				print( "Some Error occured")
				return -1,-1,-1,-1
		elif "Greyjoy Start Pos" in settings[0]:
			if(settings[1]=="YES"):
				print( "Greyjoy Start Pos:","YES")
				gj_start = 1
			elif(settings[1]=="NO"):
				print( "Greyjoy Start Pos:","NO")
				gj_start = 0
			else:
				print( "Some Error occured")
				return -1,-1,-1,-1
		elif "Lannister Ship" in settings[0]:
			if(settings[1]=="YES"):
				print( "Lannister Ship:","YES")
				lani_ship = 1
			elif(settings[1]=="NO"):
				print( "Lannister Ship:","NO")
				lani_ship = 0
			else:
				print( "Some Error occured")
				return -1,-1,-1,-1

	return tob,house_cards,lani_ship,gj_start

def is_rated(soup):
	if(soup.findAll('table')[3].find('tr').text.split(' ', 1)[0]!="\nRATED"):
		print( "Unrated game")
		return "unrated"
	else:
		return "rated"

def get_Date(soup):
	return str(soup('table')[1].findAll('tr')[-2].findAll('td')[3].text.split(',', 1)[0])







