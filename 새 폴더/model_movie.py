class Movie:

    def __init__(self, _rank, _title, _genre):
        self.rank = _rank
        self.title = _title
        self.genre = _genre

    def ShowMovie(self, _count):
        self.count = _count
        print('{0}: 순위: {1} 제목: {2} 장르: {3}'.format(self.count, self.rank, self.title, self.genre))
    