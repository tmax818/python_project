class Game:

    wins = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    def __init__(self, *players) -> None:
        self.board = list(range(1, 10))
        self.players = players
        self.turn_count = 0
        self.display_board()
        self.play_game()

    def display_board(self):

        print(f"""
        {self.board[0]} | {self.board[1]} | {self.board[2]}
        {"-" * 10}
        {self.board[3]} | {self.board[4]} | {self.board[5]}
        {"-" * 10}
        {self.board[6]} | {self.board[7]} | {self.board[8]}
        """)

    def move(self, player):
        square = int(input(f"Where would you like to move {player.name} ?"))
        if not self.is_taken(square) and not self.is_winner():
            self.board[square - 1] = player.symbol
            self.turn_count += 1
            self.display_board()
        else:
            print("What are you trying to pull?")

    def is_taken(self, square):
        return square not in self.board

    def is_winner(self):
        print('hi')
        for win in self.wins:
            a, b, c = win
            if self.board[a] == self.board[b] and self.board[b] == self.board[c] and self.board[a] == self.board[c]:
                print(self.board)
                return self.board[a]
            else:
                return False

    def take_turn(self):
        if not self.is_winner():
            if self.turn_count % 2 == 0:
                self.move(self.players[0])
            else:
                self.move(self.players[1])

    def play_game(self):
        while not self.is_winner():
            self.take_turn()
        print(self.is_winner(), "is the winner!")
        return False
