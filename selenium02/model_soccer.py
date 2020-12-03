class Soccer:

    def __init__(self, _rank, _name, _score,_nation, _team):
        self.rank = _rank
        self.name = _name
        self.score = _score
        self.nation = _nation
        self.team = _team



    def Saveline(self):
        line = '{0};{1};{2};{3};{4}\n'.format(self.rank, self.name, self.score, self.nation, self.team)


        return line



