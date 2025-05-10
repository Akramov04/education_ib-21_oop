from abc import abstractmethod, ABC


class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def __str__(self):
        return f"Engine: {self.engine_type}"

class Transmission:
    def __init__(self, transmission_type):
        self.transmission_type = transmission_type

    def __str__(self):
        return f"Transmission: {self.transmission_type}"

class Body:
    def __init__(self, body_type, color):
        self.body_type = body_type
        self.color = color

    def __str__(self):
        return f"Body: {self.body_type}, Color: {self.color}"

# Класс Car для представления автомобиля
class Car:
    def __init__(self):
        self.engine = None
        self.transmission = None
        self.body = None

    def set_engine(self, engine):
        self.engine = engine

    def set_transmission(self, transmission):
        self.transmission = transmission

    def set_body(self, body):
        self.body = body

    def __str__(self):
        return f"Car Details:\n{self.body}\n{self.engine}\n{self.transmission}"

class CarBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_engine(self):
        pass

    @abstractmethod
    def set_transmission(self):
        pass

    @abstractmethod
    def set_body(self):
        pass

    @abstractmethod
    def get_car(self) -> Car:
        pass

class SedanBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def reset(self):
        self.car = Car()

    def set_engine(self):
        self.car.set_engine(Engine("V6"))

    def set_transmission(self):
        self.car.set_transmission(Transmission("Automatic"))

    def set_body(self):
        self.car.set_body(Body("Sedan", "Red"))

    def get_car(self) -> Car:
        return self.car

class SUVBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def reset(self):
        self.car = Car()

    def set_engine(self):
        self.car.set_engine(Engine("V8"))

    def set_transmission(self):
        self.car.set_transmission(Transmission("Manual"))

    def set_body(self):
        self.car.set_body(Body("SUV", "Black"))

    def get_car(self) -> Car:
        return self.car

class SportsCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def reset(self):
        self.car = Car()

    def set_engine(self):
        self.car.set_engine(Engine("Electric"))

    def set_transmission(self):
        self.car.set_transmission(Transmission("Automatic"))

    def set_body(self):
        self.car.set_body(Body("Coupe", "Yellow"))

    def get_car(self) -> Car:
        return self.car

class CarDirector:
    def __init__(self, builder: CarBuilder):
        self.builder = builder

    def construct_car(self) -> Car:
        self.builder.reset()
        self.builder.set_engine()
        self.builder.set_transmission()
        self.builder.set_body()
        return self.builder.get_car()

if __name__ == "__main__":
    sedan_builder = SedanBuilder()
    suv_builder = SUVBuilder()
    sports_car_builder = SportsCarBuilder()

    director = CarDirector(sedan_builder)
    sedan = director.construct_car()
    print("Создан седан:")
    print(sedan)

    director = CarDirector(suv_builder)
    suv = director.construct_car()
    print("\nСоздан внедорожник:")
    print(suv)

    director = CarDirector(sports_car_builder)
    sports_car = director.construct_car()
    print("\nСоздан спорткар:")
    print(sports_car)