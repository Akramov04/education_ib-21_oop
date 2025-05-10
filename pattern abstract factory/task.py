from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

class ElectricCar(Car):
    def drive(self):
        return "Driving an electric car."

class PetrolCar(Car):
    def drive(self):
        return "Driving a petrol car."

class HybridCar(Car):
    def drive(self):
        return "Driving a hybrid car."

class CarFactory(ABC):
    @abstractmethod
    def produce_car(self) -> Car:
        pass

class ElectricCarFactory(CarFactory):
    def produce_car(self) -> Car:
        return ElectricCar()

class PetrolCarFactory(CarFactory):
    def produce_car(self) -> Car:
        return PetrolCar()

class HybridCarFactory(CarFactory):
    def produce_car(self) -> Car:
        return HybridCar()

if __name__ == "__main__":
    # Создаем фабрики
    electric_factory = ElectricCarFactory()
    petrol_factory = PetrolCarFactory()
    hybrid_factory = HybridCarFactory()

    electric_car = electric_factory.produce_car()
    petrol_car = petrol_factory.produce_car()
    hybrid_car = hybrid_factory.produce_car()

    print(electric_car.drive())  # Output: Driving an electric car.
    print(petrol_car.drive())    # Output: Driving a petrol car.
    print(hybrid_car.drive())    # Output: Driving a hybrid car.