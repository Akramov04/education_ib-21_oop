class LightingSystem:
    def turn_on(self):
        return "Свет включен."

    def turn_off(self):
        return "Свет выключен."

    def dim_lights(self):
        return "Свет приглушен."

    def get_status(self):
        return "Состояние света: включено" if self.is_on else "Состояние света: выключено"

    def __init__(self):
        self.is_on = False


class ClimateControlSystem:
    def set_comfortable_temperature(self):
        return "Температура установлена на комфортный уровень (22°C)."

    def lower_temperature(self):
        return "Температура снижена до экономичного уровня (18°C)."

    def get_status(self):
        return "Состояние климат-контроля: активен"


class SecuritySystem:
    def arm_system(self):
        return "Сигнализация включена."

    def disarm_system(self):
        return "Сигнализация отключена."

    def get_status(self):
        return "Состояние сигнализации: включена" if self.is_armed else "Состояние сигнализации: выключена"

    def __init__(self):
        self.is_armed = False


class MultimediaSystem:
    def play_music(self):
        return "Музыка включена."

    def stop_music(self):
        return "Музыка выключена."

    def get_status(self):
        return "Состояние мультимедийной системы: активна"


class SmartHomeFacade:
    def __init__(self):
        self.lighting = LightingSystem()
        self.climate = ClimateControlSystem()
        self.security = SecuritySystem()
        self.multimedia = MultimediaSystem()

    def home_mode(self):
        results = [
            self.lighting.turn_on(),
            self.climate.set_comfortable_temperature(),
            self.security.disarm_system()
        ]
        return results

    def away_mode(self):
        results = [
            self.lighting.turn_off(),
            self.multimedia.stop_music(),
            self.security.arm_system()
        ]
        return results

    def party_mode(self):
        results = [
            self.lighting.dim_lights(),
            self.multimedia.play_music(),
            self.climate.set_comfortable_temperature()
        ]
        return results

    def night_mode(self):
        results = [
            self.lighting.turn_off(),
            self.climate.lower_temperature(),
            self.security.arm_system()
        ]
        return results

    def get_all_systems_status(self):
        statuses = [
            self.lighting.get_status(),
            self.climate.get_status(),
            self.security.get_status(),
            self.multimedia.get_status()
        ]
        return "\n".join(statuses)


def main():
    print("=== Тестирование паттерна Фасад для умного дома ===")

    smart_home = SmartHomeFacade()

    print("\n1. Начальное состояние всех систем:")
    print(smart_home.get_all_systems_status())

    print("\n2. Активация режима 'Я дома':")
    home_results = smart_home.home_mode()
    for result in home_results:
        print(f" - {result}")

    print("\n   Состояние систем после активации режима 'Я дома':")
    print(smart_home.get_all_systems_status())

    print("\n3. Активация режима 'Вечеринка':")
    party_results = smart_home.party_mode()
    for result in party_results:
        print(f" - {result}")

    print("\n   Состояние систем после активации режима 'Вечеринка':")
    print(smart_home.get_all_systems_status())

    print("\n4. Активация режима 'Ночь':")
    night_results = smart_home.night_mode()
    for result in night_results:
        print(f" - {result}")

    print("\n   Состояние систем после активации режима 'Ночь':")
    print(smart_home.get_all_systems_status())

    print("\n5. Активация режима 'Я ухожу':")
    away_results = smart_home.away_mode()
    for result in away_results:
        print(f" - {result}")

    print("\n   Состояние систем после активации режима 'Я ухожу':")
    print(smart_home.get_all_systems_status())

    print("\n=== Тестирование завершено ===")


if __name__ == "__main__":
    main()