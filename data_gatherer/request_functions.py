import io
import csv
import time

from config import DATA_FOLDER, API_KEY
import requests


def save_meta_match_data(number_of_lines, server):
    meta_file_name = DATA_FOLDER + '\\meta_data'
    with io.open(meta_file_name, 'a', encoding='utf-8') as mf:
        mf.write('Przerobiono ' + str(number_of_lines) + ' linii ' + str(server) + '\n')
    print('PAMIĘTAJ ŻEBY ZAJRZEĆ DO META DANYCH I POPRAWIĆ!!!1111oneoneon')


def choose_tier(answer=None):
    if answer is None:
        print('wybierz tier: ')
        print('1. CHALLENGER')
        print('2. GRANDMASTER')
        print('3. MASTER')
        print('4. DIAMOND')
        print('5. PLATINUM')
        print('6. GOLD')
        print('7. SILVER')
        print('8. BRONZE')
        print('9. IRON')
        good_answer = False
        possible_options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        while not good_answer:
            choosen_option = input('podaj numer: ')
            if choosen_option not in possible_options:
                print('podałeś złą opcję podaj jeszcze raz')
            else:
                good_answer = True
    else:
        choosen_option = answer
    if int(str(choosen_option)) == 1:
        return 'CHALLENGER'
    elif int(str(choosen_option)) == 2:
        return 'GRANDMASTER'
    elif int(str(choosen_option)) == 3:
        return 'MASTER'
    elif int(str(choosen_option)) == 4:
        return 'DIAMOND'
    elif int(str(choosen_option)) == 5:
        return 'PLATINUM'
    elif int(str(choosen_option)) == 6:
        return 'GOLD'
    elif int(str(choosen_option)) == 7:
        return 'SILVER'
    elif int(str(choosen_option)) == 8:
        return 'BRONZE'
    elif int(str(choosen_option)) == 9:
        return 'IRON'
    else:
        print('coś źle poszło')


def choose_division():
    print('wybierz dywizję: ')
    print('1. I')
    print('2. II')
    print('3. III')
    print('4. IV')
    good_answer = False
    possible_options = ['1', '2', '3', '4']
    while not good_answer:
        choosen_option = input('podaj numer: ')
        if choosen_option not in possible_options:
            print('podałeś złą opcję podaj jeszcze raz')
        else:
            good_answer = True
    if int(str(choosen_option)) == 1:
        return 'I'
    elif int(str(choosen_option)) == 2:
        return 'II'
    elif int(str(choosen_option)) == 3:
        return 'III'
    elif int(str(choosen_option)) == 4:
        return 'IV'
    else:
        print('coś źle poszło')


def choose_server():
    print('wybierz serwer: ')
    print('1. RU')
    print('2. KR')
    print('3. BR1')
    print('4. OC1')
    print('5. JP1')
    print('6. NA1')
    print('7. EUN1')
    print('8. EUW1')
    print('9. TR1')
    print('10. LA1')
    print('11. LA2')
    good_answer = False
    possible_options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
    while not good_answer:
        choosen_option = input('podaj numer: ')
        if choosen_option not in possible_options:
            print('podałeś złą opcję podaj jeszcze raz')
        else:
            good_answer = True
    if int(str(choosen_option)) == 1:
        return 'RU'
    elif int(str(choosen_option)) == 2:
        return 'KR'
    elif int(str(choosen_option)) == 3:
        return 'BR1'
    elif int(str(choosen_option)) == 4:
        return 'OC1'
    elif int(str(choosen_option)) == 5:
        return 'JP1'
    elif int(str(choosen_option)) == 6:
        return 'NA1'
    elif int(str(choosen_option)) == 7:
        return 'EUN1'
    elif int(str(choosen_option)) == 8:
        return 'EUW1'
    elif int(str(choosen_option)) == 9:
        return 'TR1'
    elif int(str(choosen_option)) == 10:
        return 'LA1'
    elif int(str(choosen_option)) == 11:
        return 'LA2'
    else:
        print('coś źle poszło')


def parse_matches(actual_server, line):
    file_name = DATA_FOLDER + '\\matches_' + actual_server
    list_of_matches = [line.rstrip('\n') for line in io.open(file_name, encoding='utf-8')]
    counter = int(line)
    for i in range(int(line), len(list_of_matches)):
        if counter % 10 == 0:
            print('Przerobione ' + str(counter) + ' meczy serwera ' + actual_server)
        if counter - int(line) > 100:
            return [100, counter]
        request_url = 'https://' + actual_server + '.api.riotgames.com/lol/match/v4/matches/' + list_of_matches[
            i] + '?api_key=' + API_KEY
        status = 0
        while status != 200 and status != 404:
            response = requests.get(request_url)
            if response.status_code == 200:
                status = 200
            elif response.status_code == 429:
                print('Wyszło łącznie: ' + str(counter) + ' przerobionych meczy na ' + actual_server)
                print('Za dużo pobrań na raz, zmiana serwera')
                return [429, counter]
            elif response.status_code == 503:
                print('Serwis się zwiesił poczekaj chwilkę')
                time.sleep(5)
            elif response.status_code == 404:
                print('Serwis się nie znalazł')
                status = 404
            elif response.status_code == 500:
                print('Błąd serwisu')
                status = 500
            else:
                print('Wyszło łącznie: ' + str(counter) + ' przerobionych meczy na ' + actual_server)
                return [response.status_code, counter]
        if status == 404:
            counter += 1
            continue

        data = response.json()
        season_id = int(data['seasonId'])
        queue_id = int(data['queueId'])
        game_id = int(data['gameId'])
        game_version = data['gameVersion']
        platform = data['platformId']
        if data['teams'][0]['win'] == 'Win':
            win = 'team_1'
        else:
            win = 'team_2'
        if season_id != 13 or queue_id != 420:
            continue
        team_1 = [[data['participantIdentities'][0]['player']['accountId'], int(data['participants'][0]['championId'])],
                  [data['participantIdentities'][1]['player']['accountId'], int(data['participants'][1]['championId'])],
                  [data['participantIdentities'][2]['player']['accountId'], int(data['participants'][2]['championId'])],
                  [data['participantIdentities'][3]['player']['accountId'], int(data['participants'][3]['championId'])],
                  [data['participantIdentities'][4]['player']['accountId'], int(data['participants'][4]['championId'])]]

        team_2 = [[data['participantIdentities'][5]['player']['accountId'], int(data['participants'][5]['championId'])],
                  [data['participantIdentities'][6]['player']['accountId'], int(data['participants'][6]['championId'])],
                  [data['participantIdentities'][7]['player']['accountId'], int(data['participants'][7]['championId'])],
                  [data['participantIdentities'][8]['player']['accountId'], int(data['participants'][8]['championId'])],
                  [data['participantIdentities'][9]['player']['accountId'], int(data['participants'][9]['championId'])]]

        filename = DATA_FOLDER + '\\parsed_matches.csv'
        with open(filename, mode='a+', newline='') as employee_file:
            employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            employee_writer.writerow([str(season_id), str(queue_id), str(game_id), game_version, platform, win,
                                      team_1[0][0], team_1[0][1],
                                      team_1[1][0], team_1[1][1],
                                      team_1[2][0], team_1[2][1],
                                      team_1[3][0], team_1[3][1],
                                      team_1[4][0], team_1[4][1],
                                      team_2[0][0], team_2[0][1],
                                      team_2[1][0], team_2[1][1],
                                      team_2[2][0], team_2[2][1],
                                      team_2[3][0], team_2[3][1],
                                      team_2[4][0], team_2[4][1]])
        counter += 1
    print("przerobiliśmy serwer: " + actual_server)
    return True