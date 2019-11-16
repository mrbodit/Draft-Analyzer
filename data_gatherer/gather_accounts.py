import requests
from config import API_KEY, DATA_FOLDER
from data_gatherer.request_functions import choose_tier, choose_division, choose_server
import io

tier = choose_tier()
division = choose_division()
server = choose_server()
fileName = DATA_FOLDER + '\\accounts_' + server
page = input("Wybierz stronę: ")
request_URL = "https://" + server + ".api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/" + tier + "/" + division + "?page=" + page + "&api_key=" + API_KEY

response = requests.get(request_URL)

if response.status_code != 200:
    print(response.status_code)
    print(response.headers)
else:
    print("super, przeszło")
    data = response.json()
    list_of_summoners = []
    for i in range(len(data)):
        list_of_summoners.append(data[i]["summonerName"])

    list_of_saved_accounts = [line.rstrip('\n') for line in io.open(fileName, encoding="utf-8")]

    print("Ilość pobranych kont wynosi: " + str(len(list_of_summoners)))

    number_of_duplicates = 0
    list_of_duplicates = []
    for x in range(len(list_of_summoners)):
        if list_of_summoners[x] in list_of_saved_accounts:
            number_of_duplicates += 1
            list_of_duplicates.append(x)

    print("Tyle jest powtórzeń z już zapisanymi kontami: " + str(number_of_duplicates))
    save = input("Czy chcesz dopisać te które się nie powtórzyły? ")
    if save == "tak":
        print(list_of_summoners)
        print("zapisuję")
        with io.open(fileName, 'a', encoding="utf-8") as f:
            for x in range(len(list_of_summoners)):
                if x not in list_of_duplicates:
                    f.write("%s\n" % str(list_of_summoners[x]))
    else:
        print("nie zapisano")
