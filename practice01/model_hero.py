class HeroModel:

    def __init__(self, _name, _nation, _age, _ishero):
         self.name = _name
         self.nation = _nation
         self.age = _age
         self.ishero = _ishero


    def showprofile(self):
        print('국가: {0} 이름: {1} ({2})'.format(self.nation, self.name, self.age))


    def Writeline(self):
        return '{0};{1};{2};{3}\n'.format(self.nation, self.name, self.age, self.ishero)

    
    def upper(self):
        return self.name.upper()


    def lower(self):
        return self.name.lower()

