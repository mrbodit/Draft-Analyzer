servers = ['EUN1', 'EUW1', 'KR', 'TR1', 'NA1']
lines = []
for server in range(len(servers)):
    lines.append(input('Podaj linię od której zacząć parsować mecze na ' + servers[server] + ': '))

parsed = False
loop_number = 0


def parse_matches(actual_server, param):
    pass


while not parsed:
    server_index = loop_number % len(servers)
    actual_server = servers[server_index]
    response = parse_matches(actual_server, lines[server_index])
    if response == True:
        if len(servers) > 1:
            print('Serwer ' + servers[server_index] + ' przerobiony!')
            servers.pop(server_index)
        else:
            parsed = True
    else:
        print(actual_server, response)
        loop_number += 1

