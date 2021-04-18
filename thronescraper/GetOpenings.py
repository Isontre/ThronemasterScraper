from bs4 import BeautifulSoup

def Get_Opening(soup:BeautifulSoup,House:str)-> tuple: 

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
		try:
			L_LAp = soup.find("div", {"id": "Order52"}).get('class')[1] if soup.find("div", {"id": "Order18"}).get('class') else 'none'
		except:
			L_LAp = None
		return [["Lannisport",L_LA],["Stoney Sept",L_SS],["Golden Sound",L_GS],["Lannisportport",L_LAp]]
	else:
		print( "Error, House not found")
		return 0
	
