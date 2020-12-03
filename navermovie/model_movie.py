class Movie:
    def __init__(self, _code, _title, _story, _genre, _rating, _rn_tm, _op_dt):
        self.code = _code
        self.title = _title
        self.story = _story
        self.genre = _genre
        self.rating = _rating
        self.rn_tm = _rn_tm
        self.op_dt = _op_dt

    def show(self, _count):
        count = _count
        print('{0}, {1}, {2}'.format(self.count, self.code, self.title))