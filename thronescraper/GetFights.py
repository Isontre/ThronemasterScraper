import re


def Get_Fights(soup):

	list=[]
	for elem in soup(text=re.compile(r'\[Attack\]')):
		
		#print( elem.parent
		#roundnumber=elem.parent.parent.parent.findChildren('th')[0].text
		#print( roundnumber
			
		
		text=elem.parent.text
		try:
			list.append(re.search(r"([a-zA-Z]+) is attacking ([a-zA-Z]+) in ([a-zA-Z' ]+) from ([a-zA-Z' ]+) wit",text).groups())
		except:
			print( "Exception Raised",text)
			list.append(re.search(r"([a-zA-Z]+) is attacking ([a-zA-Z]+) in ([a-zA-Z' ]+) from ([a-zA-Z']+)",text).groups())
	

	return list

	