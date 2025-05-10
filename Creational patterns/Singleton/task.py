class GameSettings:
    _instance = None

    def __init__(self):
        if GameSettings._instance is not None:
            raise Exception("Этот класс является Singleton")
        self.volume = 50
        self.difficulty = "Normal"

    @staticmethod
    def get_instance():
        if GameSettings._instance is None:
            GameSettings._instance = GameSettings()
        return GameSettings._instance

if __name__ == "__main__":
    settings1 = GameSettings.get_instance()
    settings2 = GameSettings.get_instance()

    print(settings1 is settings2)

    settings1.volume = 70
    settings1.difficulty = "Hard"

    print(settings2.volume)
    print(settings2.difficulty)