from abc import ABC, abstractmethod

# State Pattern: Game State
class GameState(ABC):
    @abstractmethod
    def handle_input(self, row, col):
        pass

    @abstractmethod
    def render_board(self):
        pass

# Concrete Game State: In Progress
class InProgressState(GameState):
    def __init__(self, game):
        self.game = game

    def handle_input(self, row, col):
        if self.game.board[row][col] != " ":
            print("Cell already taken! Choose another.")
            return

        self.game.board[row][col] = self.game.current_player
        self.game.notify_observers()
        if self.game.check_winner():
            self.game.set_state(self.game.won_state)
        elif self.game.check_draw():
            self.game.set_state(self.game.draw_state)
        else:
            self.game.switch_player()

    def render_board(self):
        self.game.render()

# Concrete Game State: Won
class WonState(GameState):
    def __init__(self, game):
        self.game = game

    def handle_input(self, row, col):
        print(f"Game over! Player {self.game.current_player} has already won!")

    def render_board(self):
        self.game.render()
        print(f"Player {self.game.current_player} wins!")

# Concrete Game State: Draw
class DrawState(GameState):
    def __init__(self, game):
        self.game = game

    def handle_input(self, row, col):
        print("Game over! It's a draw!")

    def render_board(self):
        self.game.render()
        print("It's a draw!")

# Observer Pattern: Observer
class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

# Concrete Observer: ConsoleNotifier
class ConsoleNotifier(Observer):
    def update(self):
        print("Board updated.")

# Strategy Pattern: Player Strategy
class PlayerStrategy(ABC):
    @abstractmethod
    def get_move(self):
        pass

# Concrete Strategy: Human Player
class HumanPlayerStrategy(PlayerStrategy):
    def get_move(self):
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        return row, col

# Tic Tac Toe Game
class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.in_progress_state = InProgressState(self)
        self.won_state = WonState(self)
        self.draw_state = DrawState(self)
        self.state = self.in_progress_state
        self.observers = []

    def attach_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

    def set_state(self, state):
        self.state = state

    def render(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def check_draw(self):
        return all(cell != " " for row in self.board for cell in row)

    def play(self, player_strategy):
        self.attach_observer(ConsoleNotifier())
        while isinstance(self.state, InProgressState):
            self.state.render_board()
            row, col = player_strategy.get_move()
            self.state.handle_input(row, col)
        self.state.render_board()

# Main function
if __name__ == "__main__":
    game = TicTacToe()
    strategy = HumanPlayerStrategy()
    game.play(strategy)
