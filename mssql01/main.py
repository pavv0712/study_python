from adp_k_league import Searchteam
from adp_k_table import Searchtable
from adp_average import Searchaverage

command = ''


while command.upper != 'EXIT':

    command = input('명령입력요망')

    if command == '1':
        teams = Searchteam()
        for t in teams:
            t.show()

    elif command == '2':
        tables = Searchtable()
        for ta in tables:
            ta.show()

    elif command == '3':
        averages = Searchaverage()
        for ave in averages:
            ave.show()





    








