from PizzaBuilder import *
from Pizza import *

def main():
    pizzaBuilder = PizzaBuilder()
    pizza = pizzaBuilder.setDough("Thin").setCheese("Camambert").setTomatoes("Cherry").setChicken(True).setOlive(True).build()

    pizza.printPizza()

if __name__ == "__main__":
    main()
