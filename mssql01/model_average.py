class Average:
    def __init__(self, _win, _draw, _lose):
        self.win = _win
        self.draw = _draw
        self.lose = _lose


    def show(self):
        print('{0}{1}{2}'.format(self.win, self.draw, self.lose))
