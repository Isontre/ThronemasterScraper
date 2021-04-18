from thronescraper.misc import get_numbers,last_number
from thronescraper import cook_soup
from thronescraper.GetWinners import get_winner
from thronescraper.misc import Page,soup_from_html,loadPage

winner_filename = "data/winners.txt"

numbers = get_numbers()

last = last_number(winner_filename)
	

page = Page("http://game.thronemaster.net/?game="+str(numbers[0]))
for number in numbers:
    if(int(number)<=last):
        continue
    url="http://game.thronemaster.net/?game="+str(number)
    print( '-----------------------------------------------------')
    print( number,"/",numbers[-1])

    page.open(url)

    soup = soup_from_html(page.html)

    print("Calling:",url)
    winner = get_winner(soup)
    print(winner)
	
    with open(winner_filename, 'a') as the_file:
        the_file.write('%s,%s\n'%(number,winner))

