class Lamp:
    def __init__(self, lamp_state):
        self.lamp_state = lamp_state

    def turnOn(self):
        self.lamp_state = True
        print("Turning ON lamp")

    def turnOff(self):
        self.lamp_state = False
        print("Turning OFF lamp")