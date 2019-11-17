from data_gatherer.gather_accounts import gather_accounts
from data_gatherer.request_functions import choose_server, choose_tier

server = choose_server()
choosen_tier = input("wybierz od ktorego tieru zaczynamy: ")
choosen_page = input("wybierz od ktorej strony zaczynamy: ")
page = int(choosen_page)
for i in range(int(choosen_tier), 5):
    tier = choose_tier(i)
    more_pages = True
    division = "I"
    while more_pages:
        print('ZACZYNAMY TERAZ ' + server + ' ' + str(tier) + ' page: ' + str(page))
        length_of_output = gather_accounts(tier, division, server, page)
        if length_of_output == 0:
            more_pages = False
            page = 1
        else:
            page += 1
