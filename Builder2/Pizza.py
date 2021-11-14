from PizzaBuilder import *

class Pizza():

    def __init__(self, pizzaBuilder):
        self.dough = pizzaBuilder.dough
        self.cheese = pizzaBuilder.cheese
        self.tomatoes = pizzaBuilder.tomatoes
        self.chicken = pizzaBuilder.chicken
        self.pork = pizzaBuilder.pork
        self.corn = pizzaBuilder.corn
        self.pineapple = pizzaBuilder.pineapple
        self.olive = pizzaBuilder.olive

    def printPizza(self):
        print("Dough: " + str(self.dough))
        print()

        print("Cheese: " + str(self.cheese))
        print()

        if (self.tomatoes != None):
            print("Tomatoes: " + str(self.tomatoes))
            print()

        if (self.chicken != None):
            print("Chicken: " + str(self.chicken))
            print()

        if (self.pork != None):
            print("Pork: " + str(self.pork))
            print()

        if (self.corn != None):
            print("Corn: " + str(self.corn))
            print()

        if (self.pineapple != None):
            print("Pineapple: " + str(self.pineapple))
            print()

        if (self.olive != None):
            print("Olive: " + str(self.olive))
            print()
