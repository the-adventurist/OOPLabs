from abc import ABC, abstractmethod


class Cable(ABC):
    @abstractmethod
    def connect(self, d1, d2):
        pass

class HDMICable(Cable):
    def connect(self, device1, device2):
        return f"Connect {device1.__class__.__name__} to {device2.__class__.__name__} via HDMI"


class RCACable(Cable):
    def connect(self, device1, device2):
        return f"Connect {device1} to {device2} via RCA"


class EthernetCable(Cable):
    def connect(self, device1, device2):
        return f"Connect {device1} to {device2} via Ethernet"

class PowerOutlet(Cable):
    def connect(self, device1, _):
        return f"Connect device to power"


class DVDPlayer:
    pass


class GameConsole:
    pass


class Router:
    pass


class Television:
    pass


hdmi = HDMICable()
tv = Television()
gc = GameConsole()

connection1 = hdmi.connect(tv, gc)
print(connection1)