from abc import abstractmethod, ABC


class Duck(ABC):
    @staticmethod
    @abstractmethod
    def quack():
        pass


class FlyObject(ABC):
    @staticmethod
    @abstractmethod
    def fly(self):
        pass


class WalkableObject(ABC):
    @staticmethod
    @abstractmethod
    def walk():
        pass


class RubberDuck(Duck):
    @staticmethod
    def quack():
        return "Squeek"



class RobotDuck(Duck, FlyObject, WalkableObject):
    HEIGHT = 50

    def __init__(self):
        self.height = 50

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
            return f"Flying under maximum{RobotDuck.HEIGHT}"
        else:
            self.height += 1

    def land(self):
        self.height = 0




rd = RubberDuck()
print(rd.quack())
robD = RobotDuck()
print(robD.quack())
print(robD.fly())
print(robD.walk())