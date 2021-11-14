from Robot import *
from RobotBuilder import *

def main():
    robotBuilder = RobotBuilder()
    robot = robotBuilder.setHead(Head("Tech.com", "BlueGlass")).setBody(Body("SmartIndustries", "Black")).setLegs(Legs("Tech.com", "Red", 70)).setArms(Arms("SStar", "Red", 55)).setPowerGenerator(PowerGenerator("HVoltage", 550)).setGun(Gun("RockTeck", "Pistol", 9)).build()

    robot.printRobot()

if __name__ == "__main__":
    main()
