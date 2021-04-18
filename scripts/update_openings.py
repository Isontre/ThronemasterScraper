from thronescraper.misc import last_number, soup_from_html,Page
from thronescraper import cook_soup,get_numbers
from thronescraper.GetOpenings import Get_Opening

numbers = get_numbers()
	
last = last_number('Openings/OpeningStark.txt')

page = Page("")
for number in numbers:
    if(int(number)<=last):
        #Skip until you reach the last number
        continue
    url="http://game.thronemaster.net/?game="+str(number)+"&review=1"
    print( '-----------------------------------------------------')
    print( number,"/",numbers[-1])

    page.open(url)
    soup = soup_from_html(page.html)

    GJ = Get_Opening(soup,"Greyjoy")
    TY = Get_Opening(soup,"Tyrell")
    MA = Get_Opening(soup,"Martell")
    LA = Get_Opening(soup,"Lannister")
    BA = Get_Opening(soup,"Baratheon")
    ST = Get_Opening(soup,"Stark")


    with open('Openings/OpeningStark.txt', 'a') as the_file:
        the_file.write('%s,%s,%s,%s\n'%(number,ST[0][1],ST[1][1],ST[2][1]))
        
    with open('Openings/OpeningTyrell.txt', 'a') as the_file:
        the_file.write('%s,%s,%s,%s\n'%(number,TY[0][1],TY[1][1],TY[2][1]))	

    with open('Openings/OpeningBaratheon.txt', 'a') as the_file:
        the_file.write('%s,%s,%s,%s\n'%(number,BA[0][1],BA[1][1],BA[2][1]))			

    with open('Openings/OpeningLannister.txt', 'a') as the_file:
        the_file.write('%s,%s,%s,%s\n'%(number,LA[0][1],LA[1][1],LA[2][1]))
    try:
        with open('Openings/OpeningGJ.txt', 'a') as the_file:
            the_file.write('%s,%s,%s,%s,%s\n'%(number,GJ[0][1],GJ[1][1],GJ[2][1],GJ[3][1]))
    except: 
        with open('Openings/OpeningGJ.txt', 'a') as the_file:
            the_file.write('%s,%s,%s,%s\n'%(number,GJ[0][1],GJ[1][1],GJ[2][1]))

    with open('Openings/OpeningMartell.txt', 'a') as the_file:
        the_file.write('%s,%s,%s,%s\n'%(number,MA[0][1],MA[1][1],MA[2][1]))
