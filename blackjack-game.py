suit: ['']




class Board:
    def __init__(self, player, player_chip = 1, dealer_chip = 1, board_chip=0):
        self.player = player
        
        self.player_chip = player_chip
        self.dealer_chip = dealer_chip
        self.board_chip = board_chip

    def __str__(self):
        return f"Board: {self.player_chip} {self.dealer_chip}\nBoard Chip Balance: {self.board_chip}"

    def submit_chip(self, submit_chip):

        self.board_chip += self.player_chip + self.dealer_chip + submit_chip
        return f"Board: {self.board_chip}"





        

