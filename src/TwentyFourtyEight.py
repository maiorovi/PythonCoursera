""" this is fine program to play game 2048 """
import random

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    result_line = []

    for iter in range(0, len(line)):
       if (line[iter] == 0):
           continue
       result_line.append(line[iter])
    for iter in range(len(result_line), len(line)):
        result_line.append(0)

    final_result = []
    iter = 0

    while iter < len(result_line):
        if (iter + 1 == len(result_line)):
            final_result.append(result_line[iter])
            iter = iter + 1
            continue
        if (result_line[iter] == result_line[iter+1]):
            final_result.append(result_line[iter] + result_line[iter+1])
            iter = iter + 2
        elif (result_line[iter] != result_line[iter+1]):
            final_result.append(result_line[iter])
            iter = iter + 1
    for iter in range(len(final_result), len(result_line)):
        final_result.append(0)

    return final_result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._up_initial_tile = [(0, x) for x in range(self._grid_width)]
        self._down_initial_tile = [(self._grid_height - 1, x) for x in range(self._grid_width)]
        self._left_initial_tile = [(x, 0) for x in range(self.get_grid_height())]
        self._right_initial_tile = [(x, self._grid_width - 1) for x in range(self.get_grid_height())]
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for col in range(self.get_grid_width())] for row in range(self.get_grid_height())]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        result = ""

        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                result += str(self._grid[row][col]) + " "
            result += ("\n")

        return result

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        length = 0
        initial_tile = []
        should_add_tile = False

        if (direction == UP):
            length = self.get_grid_height()
            initial_tile = self._up_initial_tile
        if (direction == DOWN):
            length = self.get_grid_height()
            initial_tile = self._down_initial_tile
        if (direction == LEFT):
            length = self.get_grid_width()
            initial_tile = self._left_initial_tile
        if (direction == RIGHT):
            length = self.get_grid_width()
            initial_tile = self._right_initial_tile

        for initial_cell in initial_tile:
            row = initial_cell[0]
            col = initial_cell[1]
            temp_list = []

            for counter in range(length):
                temp_list.append(self._grid[row][col])
                row = row + OFFSETS.get(direction)[0]
                col = col + OFFSETS.get(direction)[1]

            row = initial_cell[0]
            col = initial_cell[1]
            iterator = 0
            for element in merge(temp_list):
                if (temp_list[iterator] != element):
                    should_add_tile = True
                iterator = iterator + 1
                self._grid[row][col] = element
                row = row + OFFSETS.get(direction)[0]
                col = col + OFFSETS.get(direction)[1]

        if (should_add_tile):
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        col = random.randrange(self.get_grid_width())
        row = random.randrange(self.get_grid_height())
        while (self._grid[row][col] != 0):
            col = random.randrange(self.get_grid_width())
            row = random.randrange(self.get_grid_height())
        value = random.randrange(0, 100)

        if (value > 89):
            value = 4
        else:
            value = 2

        self._grid[row][col] = value

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]
