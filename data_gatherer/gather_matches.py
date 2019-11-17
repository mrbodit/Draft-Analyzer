import io
import time

import requests

from config import DATA_FOLDER, API_KEY
from data_gatherer.request_functions import choose_server, save_meta_match_data

patch_time = 1573106400000
server = choose_server()
fileName_matches = DATA_FOLDER + '\\matches_' + server
fileName_accounts = DATA_FOLDER + '\\accounts_' + server
list_of_saved_accounts = [line.rstrip('\n') for line in io.open(fileName_accounts, encoding='utf-8')]

accounts_line = int(str(input('podaj linię z której mam zacząć wczytywać konta: ')))
for i in range(accounts_line):
    list_of_saved_accounts.pop(0)


for account in list_of_saved_accounts:
    print(list_of_saved_accounts.index(account) + accounts_line)
    list_of_saved_matches = [line.rstrip('\n') for line in io.open(fileName_matches, encoding='utf-8')]
    print(len(list_of_saved_matches))
    status = 0
    while status != 200:
        request_URL = 'https://' + server +'.api.riotgames.com/lol/match/v4/matchlists/by-account/' + account + '?queue=420&api_key=' + API_KEY
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
            save_meta_match_data(accounts_line + list_of_saved_accounts.index(account), server)
            exit()

    data = response.json()
    list_of_matches = []
    for i in range(len(data['matches'])):
        if data['matches'][i]['timestamp'] < patch_time:
            print("Wpisano " + str(i) + " meczy tego gracza i kolejny będzie już przed patchem")
            break
        if data['matches'][i]['queue'] == 420 and data['matches'][i]['season'] == 13:
            list_of_matches.append(data['matches'][i]['gameId'])
        else:
            print("mecz nie przeszedł weryfikacji")

    number_of_duplicates = 0
    list_of_duplicates = []
    with io.open(fileName_matches, 'a', encoding='utf-8') as f:
        for i in range(len(list_of_matches)):
            if str(list_of_matches[i]) in list_of_saved_matches:
                number_of_duplicates += 1
                list_of_duplicates.append(i)
            else:
                f.write('%s\n' % str(list_of_matches[i]))
    print('Na tym koncie było zagranych ' + str(len(list_of_matches)) + ' meczy od ostatniego patcha')
    print('Powtórzyło się ' + str(number_of_duplicates) + ' meczy')

save_meta_match_data(accounts_line + len(list_of_saved_accounts), server)
