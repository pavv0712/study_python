class Trip:
    def __init__(self, _name, _age, _year, _ismarried):
        self.name = _name
        self.age = _age
        self.year = _year
        self.ismarried = _ismarried

    def writeline(self):
        line = '{0};{1};{2};{3}\n'.format(self.name, self.age, self.year, self.ismarried)
        
        
        return line
