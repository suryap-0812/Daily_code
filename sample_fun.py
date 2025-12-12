class player:
    # name = "player1"
    score = 0

    def __init__(self, name):
        self.name = name

    def add_point(self, point):
        self.score += point
        if self.score < 100: self.add_point(20)
        return self.score


class game(player):
    _box = [1, 0]
    
    def game_logic(self, answer):
        if (answer in [1, 0]):
            return self.add_point(10)
        return 0
    
if __name__ == "__main__":
    g = game("Surya")
    choice = 0
    print(g.game_logic(choice))