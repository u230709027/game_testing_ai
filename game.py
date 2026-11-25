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
        self.has_key = False
    def is_wall(self, row, col):
        char = self.map[row][col]
        if char == "#":
            return True
        if char == "D" and not self.has_key:
            return True
        return False

    def move(self, d_row, d_col):
        new_row = self.player_row + d_row
        new_col = self.player_col + d_col
        if not self.is_wall(new_row, new_col):
            self.player_row = new_row
            self.player_col = new_col
            if self.map[self.player_row][self.player_col] == "K":
                self.has_key = True
                