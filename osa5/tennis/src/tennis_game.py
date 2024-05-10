class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.tennis_scores = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score +=  1
        else:
            self.player2_score += 1
            
    def get_score(self):
        
        if self.player1_score == self.player2_score:
            return self.even_score(self.player1_score)
                
        elif self.check_if_winner(self.player1_score, self.player2_score):
            return self.get_winner(self.player1_score, self.player2_score)
        
        elif self.check_if_advantage(self.player2_score, self.player1_score):
            return self.get_result(self.player1_score, self.player2_score)
        
        else:
            return self.get_points(self.player1_score, self.player2_score)
    
    def even_score(self, score):
        if score == 4:
            return "Deuce"
        else:
            return self.tennis_scores[score] + "-All"
    
    def check_if_winner(self, score, opponent):
        if score >= 4 and score-opponent >= 2:
            return True
        return False
    
    def get_winner(self, score1, score2):
        if score1 > score2:
            return "Win for player1"
        else: return "Win for player2"
    
    def check_if_advantage(self, score, opponent):
        if score >= 4 and score-opponent == 1:
            return True
        return False
    
    def get_result(self, score1, score2):
        if score1 > score2:
            return "Advantage for player1"
        else: return "Advantage for player2"
        
    def get_points(self, p1, p2):
        return self.tennis_scores[p1] + "-" + self.tennis_scores[p2]