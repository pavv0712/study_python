class Movie2:
    def __init__(self, _code, _title, _genre, _story, _img_src):
        self.code = _code
        self.title = _title
        self.genre = _genre
        self.story = _story
        self.img_src = _img_src
        
    def show(self, _count):
        self.count = _count
        print('{0}: {1} {2} {3}'.format(self.count, self.code, self.title, self.genre))


