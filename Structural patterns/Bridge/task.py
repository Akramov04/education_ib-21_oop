from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def set_state(self, state):
        pass

class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()

    def set_state(self, state):
        self.device.set_state(state)

class TV(Device):
    def __init__(self, brand):
        self.brand = brand
        self.state = "off"
        self.channel = None

    def turn_on(self):
        self.state = "on"
        print(f"{self.brand} TV включен.")

    def turn_off(self):
        self.state = "off"
        print(f"{self.brand} TV выключен.")

    def set_state(self, channel):
        if self.state == "on":
            self.channel = channel
            print(f"{self.brand} TV переключен на канал: {channel}")
        else:
            print(f"{self.brand} TV выключен. Невозможно изменить канал.")

class Light(Device):
    def __init__(self, brand):
        self.brand = brand
        self.state = "off"
        self.brightness = None

    def turn_on(self):
        self.state = "on"
        print(f"{self.brand} лампочка включена.")

    def turn_off(self):
        self.state = "off"
        print(f"{self.brand} лампочка выключена.")

    def set_state(self, brightness):
        if self.state == "on":
            self.brightness = brightness
            print(f"{self.brand} лампочка установлена на яркость: {brightness}")
        else:
            print(f"{self.brand} лампочка выключена. Невозможно изменить яркость.")

class SonyTV(TV):
    def __init__(self):
        super().__init__("Sony")

class SamsungTV(TV):
    def __init__(self):
        super().__init__("Samsung")

class PhilipsLight(Light):
    def __init__(self):
        super().__init__("Philips")

class IKEALight(Light):
    def __init__(self):
        super().__init__("IKEA")

def main():
    sony_tv = SonyTV()
    samsung_tv = SamsungTV()
    philips_light = PhilipsLight()
    ikea_light = IKEALight()

    remote_for_sony = RemoteControl(sony_tv)
    remote_for_samsung = RemoteControl(samsung_tv)
    remote_for_philips = RemoteControl(philips_light)
    remote_for_ikea = RemoteControl(ikea_light)

    remote_for_sony.turn_on()
    remote_for_sony.set_state("HBO")
    remote_for_sony.turn_off()

    remote_for_samsung.turn_on()
    remote_for_samsung.set_state("CNN")
    remote_for_samsung.turn_off()

    remote_for_philips.turn_on()
    remote_for_philips.set_state("75%")
    remote_for_philips.turn_off()

    remote_for_ikea.turn_on()
    remote_for_ikea.set_state("50%")
    remote_for_ikea.turn_off()

if __name__ == "__main__":
    main()