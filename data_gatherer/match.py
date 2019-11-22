class Match:
    def __init__(self, season_id, queue_id, match_id, team_1, team_2, win):
        self.season_id = season_id   #13
        self.queue_id = queue_id     #420
        self.match_id = match_id     #2313128914
        self.team_1 = team_1         #[ [account_id, champion] * 5]
        self.team_2 = team_2         #[ [account_id, champion] * 5]
        self.win = win               #team_1 or team_2
