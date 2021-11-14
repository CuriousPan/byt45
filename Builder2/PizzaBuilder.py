import Pizza

class PizzaBuilder():
    def __init__(self):
        self.dough = None
        self.cheese = None
        self.tomatoes = None
        self.chicken = None
        self.pork = None
        self.corn = None
        self.pineapple = None
        self.olive = None

    def setDough(self, dough):
        self.dough = dough
        return self

    def setCheese(self, cheese):
        self.cheese = cheese
        return self

    def setTomatoes(self, tomatoes):
        self.tomatoes = tomatoes
        return self

    def setChicken(self, chicken):
        self.chicken = chicken
        return self

    def setPork(self, pork):
        self.pork = pork
        return self

    def setCorn(self, corn):
        self.corn = corn
        return self

    def setPineapple(self, pineapple):
        self.pineapple = pineapple
        return self

    def setOlive(self, olive):
        self.olive = olive
        return self

    def build(self):
        if (self.dough == None):
            raise Exception #incomplete type
        if (self.cheese == None):
            raise Exception #incomplete type

        return Pizza.Pizza(self)
