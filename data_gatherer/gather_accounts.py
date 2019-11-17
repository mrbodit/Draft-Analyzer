import time

import requests
from config import API_KEY, DATA_FOLDER
from data_gatherer.request_functions import choose_tier, choose_division, choose_server
import io

tier = choose_tier()
division = choose_division()
server = choose_server()
file_name = DATA_FOLDER + '\\accounts_' + server
meta_file_name = DATA_FOLDER + '\\meta_data'
page = input('Wybierz stronę: ')

status = 0
while status != 200:
    request_URL = 'https://' + server + '.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/' + tier + '/' + division + '?page=' + page + '&api_key=' + API_KEY
    response = requests.get(request_URL)
    if response.status_code == 200:
        status = 200
    elif response.status_code == 429:
        print('Za dużo pobrań na raz, poczekaj dwie minutki')
        time.sleep(120)
    else:
        print(response.status_code)
        print(response.headers)
        exit()

print('super, przeszło')
data = response.json()
list_of_summoners = []
for i in range(len(data)):
    list_of_summoners.append(data[i]['summonerName'])
print('Ilość pobranych summonerów wynosi: ' + str(len(list_of_summoners)))

list_of_saved_accounts = [line.rstrip('\n') for line in io.open(file_name, encoding='utf-8')]
with io.open(file_name, 'a', encoding='utf-8') as f:
    for summoner_name in list_of_summoners:

        status = 0
        while status != 200:
            request_URL = 'https://' + server + '.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summoner_name + '?api_key=' + API_KEY
            response = requests.get(request_URL)
            if response.status_code == 429:
                print('Za dużo pobrań na raz, poczekaj dwie minutki')
                time.sleep(120)
            elif response.status_code == 503:
                print('Serwis się zwiesił poczekaj chwilkę')
                time.sleep(15)
            elif response.status_code == 200:
                status = 200
            else:
                print(response.status_code)
                print(response.headers)
                exit()

        data = response.json()
        account_name = data['accountId']

        # number_of_duplicates = 0
        # list_of_duplicates = []
        # for x in range(len(list_of_summoners)):
        #     if list_of_summoners[x] in list_of_saved_accounts:
        #         number_of_duplicates += 1
        #         list_of_duplicates.append(x)

        # print('Tyle jest powtórzeń z już zapisanymi kontami: ' + str(number_of_duplicates))
        # save = input('Czy chcesz dopisać te które się nie powtórzyły? ')
        # if save == 'tak':
        #     print(list_of_summoners)
        #     print('zapisuję')
        #     with io.open(fileName, 'a', encoding='utf-8') as f:
        #         for x in range(len(list_of_summoners)):
        #             if x not in list_of_duplicates:
        #                 f.write('%s\n' % str(list_of_summoners[x]))
        # else:
        #     print('nie zapisano')

        if account_name in list_of_summoners:
            print('dane konto juz wystąpiło')
        else:
            print('zapisano: ' + str(summoner_name) + ' ' + str(account_name))
            f.write('%s\n' % str(account_name))


with io.open(meta_file_name, 'a', encoding='utf-8') as mf:
    mf.write(str(tier) + ' ' + str(division) + ' ' + str(server) + ' ' + str(page) + ' ' + str(len(list_of_summoners)) + '\n')
print('PAMIĘTAJ ŻEBY ZAJRZEĆ DO META DANYCH I POPRAWIĆ!!!1111oneoneon')