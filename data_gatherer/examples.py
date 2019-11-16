import requests

request_URL = 'https://eun1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/DIAMOND/I?page=1&api_key=RGAPI-9e092e69-2126-4af8-a2cb-6da7182854c4'


response = requests.get(request_URL)
if response.status_code == 200:
    print('super, przeszło')
    print(response.json())
else:
    print(response.status_code)

data = response.json()
list_of_summoners = []
for i in range(len(data)):
    list_of_summoners.append(data[i]['summonerName'])

print(list_of_summoners)




request_URL = 'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + list_of_summoners[0] + '?api_key=RGAPI-9e092e69-2126-4af8-a2cb-6da7182854c4'
response = requests.get(request_URL)
if response.status_code == 200:
    print('super, przeszło')
    print(response.json())
else:
    print(response.status_code)

data = response.json()
list_of_accounts = data['accountId']

request_URL = 'https://eun1.api.riotgames.com/lol/match/v4/matchlists/by-account/eveuFNmjedu3qDfn0iHOP6pv_PNRNsQVDU3wKKq9Kk4?queue=420&season=13&beginTime=1572998400&api_key=RGAPI-9e092e69-2126-4af8-a2cb-6da7182854c4'

response = requests.get(request_URL)
if response.status_code == 200:
    print('super, przeszło')
    print(response.json())
else:
    print(response.status_code)

data = response.json()
list_of_matches = []
for i in range(len(data['matches'])):
    list_of_matches.append(data['matches'][i]['gameId'])




with open('D:\projekty\draft analyzer\Draft-Analyzer\data_gatherer\data\matches_id', 'w') as f:
    for item in list_of_matches:
        f.write('%s\n' % item)
