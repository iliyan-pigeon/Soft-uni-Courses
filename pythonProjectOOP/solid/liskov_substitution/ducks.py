from abc import abstractmethod, ABC


class Duck(ABC):
    @abstractmethod
    def quack(self):
        ...


class RubberDuck(Duck):

    def quack(self):
        return "Squeak"


class RobotDuck(Duck):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    def quack(self):
        return 'Robotic quacking'

    def land(self):
        self.height = 0

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1






