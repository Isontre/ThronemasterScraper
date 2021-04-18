

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
		print( "Error, House not found")
		return 0
	
