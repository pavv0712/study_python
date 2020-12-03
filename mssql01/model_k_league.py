class League:
    def __init__(self, _name, _year, _coach, _captain, _top_socorer, _top_helper):
        self.name = _name
        self.year = _year
        self.coach = _coach
        self.captain = _captain
        self.top_socorer = _top_socorer
        self.top_helper = _top_helper



    def show(self):
        print('{0}{1}{2}{3}'.format(self.name, self.year, self.coach, self.captain))
