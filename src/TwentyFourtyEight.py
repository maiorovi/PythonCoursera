import random

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    result_line = []

    for i in range(0, line.__len__()):
       if (line[i] == 0):
           continue
       result_line.append(line[i])
    for i in range(result_line.__len__(), line.__len__()):
        result_line.append(0)

    final_result = []
    i = 0

    while i < result_line.__len__() :
        if (i + 1 == result_line.__len__()):
            final_result.append(result_line[i])
            i = i + 1
            continue
        if (result_line[i] == result_line[i+1]):
            final_result.append(result_line[i] + result_line[i+1])
            i = i + 2
        elif (result_line[i] != result_line[i+1]):
            final_result.append(result_line[i])
            i = i + 1
    for i in range(final_result.__len__(), result_line.__len__()):
        final_result.append(0)

    return final_result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.grid = [[0 for col in range(grid_width)] for row in range(grid_height)]
        pass

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for col in range(self.get_grid_width())] for row in range(self.get_grid_height())]
        self.new_tile()
        self.new_tile()
        pass

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return ""

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        col = random.randrange(self.get_grid_width())
        row = random.randrange(self.get_grid_height())
        while (self.grid[col][row] != 0):
            col = random.randrange(self.get_grid_width())
            row = random.randrange(self.get_grid_height())
        value = random.randrange(0, 100)

        if (value > 89):
            value = 4
        else:
            value = 2

        self.grid[row][col] = value
        pass

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value
        pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]

object = TwentyFortyEight(2,5)

print object.grid
object.new_tile()
object.new_tile()
print object.grid
