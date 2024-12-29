from abc import ABC, abstractmethod

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self, snake):
        pass

# Concrete commands for each direction
class MoveUpCommand(Command):
    def execute(self, snake):
        snake.change_direction(0, -1)

class MoveDownCommand(Command):
    def execute(self, snake):
        snake.change_direction(0, 1)

class MoveLeftCommand(Command):
    def execute(self, snake):
        snake.change_direction(-1, 0)

class MoveRightCommand(Command):
    def execute(self, snake):
        snake.change_direction(1, 0)





class GameState:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameState, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        self.grid_size = 10
        self.snake = Snake()
        self.score = 0
        self.food = None

    def reset(self):
        self.snake = Snake()
        self.score = 0
        self.food = None





from random import randint

# Food classes
class Food:
    def __init__(self, points, growth):
        self.points = points
        self.growth = growth

class NormalFood(Food):
    def __init__(self):
        super().__init__(points=10, growth=1)

class SpecialFood(Food):
    def __init__(self):
        super().__init__(points=20, growth=2)

# Factory
class FoodFactory:
    @staticmethod
    def create_food():
        if randint(0, 1):  # 50% chance of special food
            return SpecialFood()
        return NormalFood()








class Snake:
    def __init__(self):
        self.body = [(5, 5)]  # Initial position
        self.direction = (0, 1)  # Initially moving down

    def change_direction(self, dx, dy):
        # Prevent reversing direction
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = (dx, dy)

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)  # Add new head
        self.body.pop()  # Remove tail

    def grow(self, growth):
        self.body.extend([self.body[-1]] * growth)  # Extend body by growth

class SnakeGame:
    def __init__(self):
        self.state = GameState()
        self.factory = FoodFactory()
        self.state.food = self.factory.create_food()

    def render(self):
        grid = [[" " for _ in range(self.state.grid_size)] for _ in range(self.state.grid_size)]
        # Draw snake
        for x, y in self.state.snake.body:
            grid[y][x] = "S"
        # Draw food
        grid[randint(0, 9)][randint(0, 9)] = "F"
        # Print grid
        for row in grid:
            print("".join(row))
        print(f"Score: {self.state.score}")

    def play(self):
        from time import sleep
        from threading import Thread

        # Input handling
        commands = {
            "w": MoveUpCommand(),
            "s": MoveDownCommand(),
            "a": MoveLeftCommand(),
            "d": MoveRightCommand(),
        }

        # def get_input():
        #     while True:

        # Start input thread
        # Thread(target=get_input, daemon=True).start()

        # Game loop
        while True:
            key = input("Enter direction (w/a/s/d): ")
            if key in commands:
                commands[key].execute(self.state.snake)
            self.state.snake.move()
            # Check collisions
            head_x, head_y = self.state.snake.body[0]
            if head_x < 0 or head_x >= self.state.grid_size or head_y < 0 or head_y >= self.state.grid_size:
                print("Game Over! You hit the wall.")
                break
            if len(self.state.snake.body) != len(set(self.state.snake.body)):
                print("Game Over! You hit yourself.")
                break
            self.render()
            sleep(1)

if __name__ == "__main__":
    game = SnakeGame()
    game.play()
