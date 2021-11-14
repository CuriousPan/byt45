from Head import *
from Body import *
from Legs import *
from Arms import *
from Gun import *
from PowerGenerator import *
from Armor import *
import Robot

class RobotBuilder():

    def __init__(self):
        self.head = None
        self.body = None
        self.legs = None
        self.arms = None
        self.gun = None
        self.powerGenerator = None
        self.armor = None

    def build(self):
        if (self.head == None):
            raise IncompleteType

        if (self.body == None):
            raise IncompleteType

        if (self.legs == None):
            raise IncompleteType

        if (self.arms == None):
            raise Exception #incomplete type

        if (self.powerGenerator == None):
            raise Exception #incomplete type
        
        return Robot.Robot(self)

    def setHead(self, head):
        self.head = head
        return self

    def setBody(self, body):
        self.body = body
        return self

    def setLegs(self, legs):
        self.legs = legs
        return self

    def setArms(self, arms):
        self.arms = arms
        return self

    def setGun(self, gun):
        self.gun = gun
        return self

    def setPowerGenerator(self, powerGenerator):
        self.powerGenerator = powerGenerator
        return self

    def setArmor(self, armor):
        self.armor = armor
        return self

