class Car:
    def __init__(self, brand):
        self.brand = brand
        self._fuel_level = 0.0
        self.__engine_status = False

    def start_engine(self):
        if self._fuel_level > 0:
            self.__engine_status = True
            print("Двигатель запущен.")
        else:
            print("Невозможно завести двигатель — нет топлива!")

    def stop_engine(self):
        self.__engine_status = False
        print("Двигатель остановлен.")

    def drive(self, distance):
        fuel_needed = distance * 0.1
        if self.__check_fuel(fuel_needed):
            self._fuel_level -= fuel_needed
            print(f"Проехали {distance} км. Осталось топлива: {self._fuel_level:.2f} л.")
        else:
            print("Недостаточно топлива для поездки!")

    def refuel(self, amount):
        if amount > 0:
            self._fuel_level += amount
            print(f"Заправлено {amount} л. Текущий уровень топлива: {self._fuel_level:.2f} л.")
        else:
            print("Количество топлива должно быть положительным!")

    def get_status(self):
        engine = "включен" if self.__engine_status else "выключен"
        return f"Марка: {self.brand}, Топливо: {self._fuel_level:.2f} л, Двигатель: {engine}"

    def __check_fuel(self, amount_needed):
        return self._fuel_level >= amount_needed