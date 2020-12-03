class Staff:
    def __init__(self, _s_code, _k_name, _e_name):
        self.s_code = _s_code
        self.k_name = _k_name
        self.e_name = _e_name


    def show(self):
        print('{0}{1}{2}'.format(self.s_code, self.k_name, self.e_name))