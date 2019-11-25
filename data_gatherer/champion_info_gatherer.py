import requests
champions = ["Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Ashe", "AurelionSol", "Azir", "Bard",
             "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia", "Chogath", "Corki", "Darius", "Diana",
             "DrMundo", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio",
             "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Hecarim", "Heimerdinger", "Illaoi", "Irelia", "Ivern",
             "Janna", "JarvanIV", "Jax", "Jayce", "Jhin", "Jinx", "Kaisa", "Kalista", "Karma", "Karthus", "Kassadin",
             "Katarina", "Kayle", "Kayn", "Kennen", "Khazix", "Kindred", "Kled", "Kogmaw", "Leblanc", "LeeSin", "Leona",
             "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "MasterYi", "MissFortune",
             "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nocturne", "Nunu", "Olaf",
             "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn", "Rakan", "Rammus", "RekSai", "Renekton",
             "Rengar", "Riven", "Rumble", "Ryze", "Sejuani", "Senna", "Shaco", "Shen", "Shyvana", "Singed", "Sion",
             "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "TahmKench", "Taliyah", "Talon", "Taric",
             "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "TwistedFate", "Twitch", "Udyr", "Urgot", "Varus",
             "Vayne", "Veigar", "Velkoz", "Vi", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah",
             "Xerath", "XinZhao", "Yasuo", "Yorick", "Yuumi", "Zac", "Zed", "Ziggs", "Zilean", "Zoe", "Zyra"]




request_url = 'http://ddragon.leagueoflegends.com/cdn/9.22.1/data/en_US/champion/Jax.json'
response = requests.get(request_url)
data = response.json()
print(data["data"]["Jax"]["key"])