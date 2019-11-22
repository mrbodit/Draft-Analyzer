import requests
import csv
from config import DATA_FOLDER, API_KEY
import time

from data_gatherer.request_functions import parse_matches

meta_file_name = DATA_FOLDER + '\\meta_data'
servers = ['EUN1', 'EUW1', 'KR', 'NA1', 'RU', 'TR1']
lines = []
for server in range(len(servers)):
    lines.append(input('Podaj linię od której zacząć parsować mecze na ' + servers[server] + ': '))

parsed = False
loop_number = 0

while not parsed:
    server_index = loop_number % len(servers)
    actual_server = servers[server_index]
    time_start = time.time()
    response = parse_matches(actual_server, lines[server_index])
    if time.time() - time_start < 20:
        print('za szybko przeszły serwery, musimy poczekać minutkę')
        time.sleep(70)
    if response == True:
        if len(servers) > 1:
            print('Serwer ' + servers[server_index] + ' przerobiony!')
            servers.pop(server_index)
        else:
            parsed = True
    else:
        lines[server_index] = response[1]
        print(actual_server, response[0])
        loop_number += 1

