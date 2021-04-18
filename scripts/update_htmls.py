
import os.path
from thronescraper import get_numbers
from thronescraper.misc import cook_soup, get_html,soup_from_html
from thronescraper.misc import Page

numbers = get_numbers()


page = Page("")
for number in numbers:
	if os.path.isfile("htmls/"+str(number)+".html"):
		continue
	url="http://game.thronemaster.net/?game="+str(number)
	print( '-----------------------------------------------------')
	print( number,"/",numbers[-1])

	page.open(url)
	html = page.html # if this doesn't work it might be an utf8 encoding problem. before it was .encode("utf-8")
	with open("htmls/"+str(number)+".html", 'w') as the_file:
		the_file.write(str(html))




for number in numbers:
	if os.path.isfile("htmls/"+str(number)+".html"):
		continue
	url="http://game.thronemaster.net/?game="+str(number)+"&show=log"
	print( '-----------------------------------------------------')
	print( number,"/",numbers[-1])
	html = cook_soup(url).encode("utf-8") # if this doesn't work it might be an utf8 encoding problem. before it was .encode("utf-8")
	with open("htmls/"+str(number)+".html", 'w') as the_file:
		the_file.write(str(html))





