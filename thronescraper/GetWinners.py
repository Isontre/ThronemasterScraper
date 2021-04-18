from bs4 import BeautifulSoup


def get_winner(soup:BeautifulSoup)->str:
	"""Gets the winner by scraping the 'right' html field

	Args:
		soup (BeautifulSoup): The soup to the log url

	Returns:
		str: Either "Lennister", "Greyjoy", etc..
	"""
	return soup.find("div", {"id": "gameStateText"}).find('b').text.split(' ', 1)[0]

