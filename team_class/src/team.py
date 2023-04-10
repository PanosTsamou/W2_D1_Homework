class Team():

    def __init__(self, input_team_name, input_players, input_coach) :
        self.name = input_team_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0 

    def add_player(self, new_player):
        self.players.append(new_player)
    
    def has_player(self, looking_for_player):
        return looking_for_player in self.players

    def play_game(self, win_lose):
        if not win_lose:
            if self.points==0:
                return
            else:
                self.points -= 3
        else:
            self.points += 3

        