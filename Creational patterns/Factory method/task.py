from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        return "Рычание!"

class Monkey(Animal):
    def make_sound(self):
        return "Визг!"

class Elephant(Animal):
    def make_sound(self):
        return "Трубление!"

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass

class LionFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Lion()

class MonkeyFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Monkey()

class ElephantFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Elephant()


def interact_with_animal(factory: AnimalFactory):
    animal = factory.create_animal()
    print(f"Звук: {animal.make_sound()}")


if __name__ == "__main__":
    lion_factory = LionFactory()
    monkey_factory = MonkeyFactory()
    elephant_factory = ElephantFactory()

    interact_with_animal(lion_factory)     # Вывод: Звук: Рычание!
    interact_with_animal(monkey_factory)   # Вывод: Звук: Визг!
    interact_with_animal(elephant_factory) # Вывод: Звук: Трубление!