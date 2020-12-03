class Table:

    def __init__(self, _rank, _name, _round, _point, _win, _draw, _lose, _gf, _gc, _gd, _help, _foul):
        self.rank = _rank
        self.name = _name
        self.round = _round
        self.point = _point
        self.win = _win
        self.draw = _draw
        self.lose = _lose
        self.gf = _gf
        self.gc = _gc
        self.gd = _gd
        self.help = _help
        self.foul = _foul

    def show(self):
        print('{0}{1}{2}{3}'.format(self.rank, self.name, self.round, self.point))

        