class Conway:
    def __init__(self):
        """
        initialize a 10x10 grid
        I know the grid in Conway's Game of Life is infinite but who cares
        """
        self.grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def print_grid(self):
        """
        print the grid
        """
        for i in self.grid:
            for j in i:
                print(j, end=" ")
            print()

    def cycle(self):
        """
        update the grid
        """
        # create an empty grid with no live cells
        # we use a second grid as to not overwrite the original grid until nesscary
        cells = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        
        # loop through the grid
        for row in range(len(self.grid)):
            for column in range(len(self.grid[0])):
                # update the cell on the new grid
                cells[row][column] = self.update_cell(row, column)

        # loop through the grid
        for row in range(len(self.grid)):
            for column in range(len(self.grid[0])):
                # update the cell on the original grid
                self.grid[row][column] = cells[row][column]

    def get_type(self, row, column):
        """
        get the type of cell (edge, corner, or normal)
        """
        # check if the cell is on the corner
        # we do this by checking if the cell's row and column is 0 or the last row or column
        is_corner = row in {0, len(self.grid) - 1} and column in {0, len(self.grid[0]) - 1}

        # check if the cell is on the edge
        # we do this by checking if the cell's row or column is 0 or the last row or column
        is_edge = row in {0, len(self.grid) - 1} or column in {0, len(self.grid[0]) - 1}

        # return the type of cell
        if is_corner:
            return "corner"
        elif is_edge:
            return "edge"
        return "normal"

    def update_cell(self, row, column):
        """
        update the cell
        """
        # create an instance of the grid to be used in the function
        grid = self.grid
        # get the state of the cell
        state = grid[row][column]
        # a list to store the section of the grid (aka the cell's neighborhs)
        section = []
        # get the type of the cell
        type_ = self.get_type(row, column)

        # check if the cell is on the corner
        if type_ == "corner":
            if row == 0:
                # check if the cell is on the top left corner
                if column == 0:
                    # add the top left corner's neighbors to the section
                    section = [
                        grid[row][column + 1], grid[row + 1][column],
                        grid[row + 1][column + 1]
                    ]

                # check if the cell is on the top right corner
                elif column == 9:
                    # add the top right corner's neighbors to the section
                    section = [
                        grid[row][column - 1], grid[row + 1][column - 1],
                        grid[row + 1][column]
                    ]

            elif row == 9:
                # check if the cell is on the bottom left corner
                if column == 0:
                    # add the bottom left corner's neighbors to the section
                    section = [
                        grid[row - 1][column], grid[row - 1][column + 1],
                        grid[row][column + 1]
                    ]

                # check if the cell is on the bottom right corner
                elif column == 9:
                    # add the bottom right corner's neighbors to the section
                    section = [
                        grid[row - 1][column - 1], grid[row - 1][column],
                        grid[row][column - 1]
                    ]

        # check if the cell is on the edge
        elif type_ == "edge":
            # check if the cell is on the top/bottom edge
            if 0 < column < 9:
                # check if the cell is on the top edge
                if row == 0:
                    # add the top nth edge's neighbors to the section
                    section = [
                        grid[row][column - 1], grid[row][column + 1],
                        grid[row + 1][column - 1], grid[row + 1][column],
                        grid[row + 1][column + 1]
                    ]

                # check if the cell is on the bottom edge
                elif row == 9:
                    # add the bottom nth edge's neighbors to the section
                    section = [
                        grid[row - 1][column - 1], grid[row - 1][column],
                        grid[row - 1][column + 1], grid[row][column - 1],
                        grid[row][column + 1]
                    ]

            # check if the cell is on the left/right edge
            elif 0 < row < 9:
                # check if the cell is on the left edge
                if column == 0:
                    # add the left nth edge's neighbors to the section
                    section = [
                        grid[row - 1][column], grid[row - 1][column + 1],
                        grid[row][column + 1], grid[row + 1][column],
                        grid[row + 1][column + 1]
                    ]

                # check if the cell is on the right edge
                elif column == 9:
                    # add the right nth edge's neighbors to the section
                    section = [
                        grid[row - 1][column - 1], grid[row - 1][column],
                        grid[row][column - 1], grid[row + 1][column - 1],
                        grid[row + 1][column]
                    ]

        # normal cell
        else:
            # add the cell's neighbors to the section
            section = [
                grid[row - 1][column - 1], grid[row - 1][column],
                grid[row - 1][column + 1], grid[row][column - 1],
                grid[row][column + 1], grid[row + 1][column - 1],
                grid[row + 1][column], grid[row + 1][column + 1]
            ]

        # get the number of live neighbors
        neighbours = sum(section)

        # apply the rules of the game
        #
        # any live cell with two or three live neighbours survives
        # all other live cells die in the next generation
        # any dead cell with three live neighbours becomes a live cell
        # all other dead cells stay dead
        if (state == 1 and neighbours in {2, 3}) or (state == 0 and neighbours == 3):
            state = 1
        else:
            state = 0

        # return the new state of the cell
        return state


    
