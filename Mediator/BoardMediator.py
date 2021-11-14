from Button import *
from Cannon import *
from Rocket import *
from MachineGun import *

class BoardMediator():

    def __init__(self):
        self.cannon = Cannon()
        self.rocket = Rocket()
        self.machineGun = MachineGun()

    def handle(self, code):
        if (code == 1):
            self.cannon.fire()
        elif (code == 2):
            self.rocket.launch()
        elif (code == 3):
            self.machineGun.fire()
