class Conway:
    def __init__(self):
        self.grid = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def print_grid(self):
        for i in self.grid:
            for j in i:
                print(j, end=" ")
            print()

    def get_str(self):
        grid_string = ""
        for i in self.grid:
            for j in i:
                grid_string += str(j) + " "
            grid_string += "\n"
        return grid_string

    def cycle(self):
        cells = [[0 for _ in range(len(self.grid))]
                 for _ in range(len(self.grid))]
        for row in range(len(self.grid)):
            for column in range(len(self.grid[0])):

                cells[row][column] = self.update_cell(row, column)
        self.grid = cells

    def get_type(self, row, column):
        if row in {0, len(self.grid) - 1} and column in {0, len(self.grid[0]) - 1}:
            return "corner"
        elif row in {0, len(self.grid) - 1} or column in {0, len(self.grid[0]) - 1}:
            return "edge"
        return "normal"

    def update_cell(self, row, column):
        grid = self.grid
        state = grid[row][column]
        section = []
        type_ = self.get_type(row, column)
        if type_ == "corner":
            if row == 0:
                if column == 0:
                    section = [
                        grid[row][column + 1], grid[row + 1][column],
                        grid[row + 1][column + 1]]

                elif column == 9:
                    section = [
                        grid[row][column - 1], grid[row + 1][column - 1],
                        grid[row + 1][column]]

            elif row == 9:
                if column == 0:
                    section = [
                        grid[row - 1][column], grid[row - 1][column + 1],
                        grid[row][column + 1]]
                elif column == 9:
                    section = [
                        grid[row - 1][column - 1], grid[row - 1][column],
                        grid[row][column - 1]]
        elif type_ == "edge":
            if 0 < column < 9:
                if row == 0:
                    section = [
                        grid[row][column - 1], grid[row][column + 1],
                        grid[row + 1][column - 1], grid[row + 1][column],
                        grid[row + 1][column + 1]]
                elif row == 9:
                    section = [
                        grid[row - 1][column - 1], grid[row - 1][column],
                        grid[row - 1][column + 1], grid[row][column - 1],
                        grid[row][column + 1]]
            elif 0 < row < 9:
                if column == 0:
                    section = [
                        grid[row - 1][column], grid[row - 1][column + 1],
                        grid[row][column + 1], grid[row + 1][column],
                        grid[row + 1][column + 1]]
                elif column == 9:
                    section = [
                        grid[row - 1][column - 1], grid[row - 1][column],
                        grid[row][column - 1], grid[row + 1][column - 1],
                        grid[row + 1][column]]
        else:
            section = [
                grid[row - 1][column - 1], grid[row - 1][column],
                grid[row - 1][column + 1], grid[row][column - 1],
                grid[row][column + 1], grid[row + 1][column - 1],
                grid[row + 1][column], grid[row + 1][column + 1]]
        neighbours = sum(section)
        state = (state == 1 and neighbours in {2, 3}) or (state == 0 and neighbours == 3)
        return state+0
        
