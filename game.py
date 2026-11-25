def load_map(path):
    with open(path) as f:
        lines = f.read().splitlines()
    return lines

class Game:
    def __init__(self, map_path):
        self.map = load_map(map_path)
        for row, line in enumerate(self.map):
            for col, char in enumerate(line):
                if char == "S":
                    self.player_row = row
                    self.player_col = col

    def is_wall(self, row, col):
        return self.map[row][col] == "#"

    def move(self, d_row, d_col):
        new_row = self.player_row + d_row
        new_col = self.player_col + d_col
        if not self.is_wall(new_row, new_col):
            self.player_row = new_row
            self.player_col = new_col