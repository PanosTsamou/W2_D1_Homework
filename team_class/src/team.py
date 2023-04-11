class Team():

        #initialise my class properties
    def __init__(self, input_team_name, input_players, input_coach) :
        self.name = input_team_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0 


    # adds a player in the list of team's players
    def add_player(self, new_player):
        self.players.append(new_player)
    

    #it takes a name and checks if he is in the team
    def has_player(self, looking_for_player):
        return looking_for_player in self.players


    #it adds  3 points if the team wins
    def play_game(self, win_lose):
        if win_lose:
            self.points += 3

        