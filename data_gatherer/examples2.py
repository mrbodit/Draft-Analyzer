import requests

fileName = 'D:\projekty\draft analyzer\Draft-Analyzer\data_gatherer\data\matches_id'

list_of_matches = [line.rstrip('\n') for line in open(fileName)]

parsed_matches = []
counter = 0
for matchID in list_of_matches:
    counter += 1
    request_URL = 'https://eun1.api.riotgames.com/lol/match/v4/matches/' + matchID + '?api_key=RGAPI-9e092e69-2126-4af8-a2cb-6da7182854c4'
    response = requests.get(request_URL)
    if response.status_code == 200:
        print(str(counter) + "super, przeszło")
    else:
        print(response.status_code)
        break
    data = response.json()
    parsed_matches.append([data['teams'][0]['win'], data['teams'][1]['win'], [data['participants'][0]['teamId'], data['participants'][0]['championId'],
                                                                              data['participants'][1]['teamId'], data['participants'][1]['championId'],
                                                                              data['participants'][2]['teamId'], data['participants'][2]['championId'],
                                                                              data['participants'][3]['teamId'], data['participants'][3]['championId'],
                                                                              data['participants'][4]['teamId'], data['participants'][4]['championId'],
                                                                              data['participants'][5]['teamId'], data['participants'][5]['championId'],
                                                                              data['participants'][6]['teamId'], data['participants'][6]['championId'],
                                                                              data['participants'][7]['teamId'], data['participants'][7]['championId'],
                                                                              data['participants'][8]['teamId'], data['participants'][8]['championId'],
                                                                              data['participants'][9]['teamId'], data['participants'][9]['championId']]])

print(parsed_matches)