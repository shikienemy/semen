import json

class Car:
    def __init__(self, brand, model, body, color, plate, gear, headlights, doors, engine):
        self.brand = brand
        self.model = model
        self.body = body
        self.color = color
        self.plate = plate
        self.gear = gear
        self.headlights = headlights
        self.doors = doors
        self.engine = engine

    def display_info(self):
        print(f"\nИнформация об автомобиле:\nМарка: {self.brand}\
        \nМодель: {self.model}\nТип кузова: {self.body}\nЦвет: {self.color}")
        print(f"Гос. номер: {self.plate}\nПривод: {self.get_gear()}\
        \nФары: {self.get_headlights_status()}")
        print(f"Двери: {self.get_doors_status()}\nСостояние двигателя: {self.get_engine_status()}")

    def get_headlights_status(self):
        return "Включены" if self.headlights == "1" else "Выключены"

    def get_doors_status(self):
        return "Открыты" if self.doors == "1" else "Закрыты"

    def get_engine_status(self):
        return "Заведен" if self.engine == "1" else "Заглушен"

    def get_gear(self):
        gears = {"1": "Передний", "2": "Задний", "3": "Полный"}
        return gears.get(self.gear, "Неверный тип привода")


class CarManager:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, plate):
        for car in self.cars:
            if car.plate == plate:
                self.cars.remove(car)
                print(f"Автомобиль с гос. номером {plate} успешно удален.")
                return
        print(f"Автомобиль с гос. номером {plate} не найден.")

    def display_cars(self):
        for car in self.cars:
            car.display_info()

    def find_car(self, plate):
        for car in self.cars:
            if car.plate == plate:
                car.display_info()
                return
        print(f"Автомобиль с гос. номером {plate} не найден.")

    def update_car(self, plate):
        for car in self.cars:
            if car.plate == plate:
                print("\nВведите новую информацию об автомобиле:")
                brand = input("Марка: ")
                model = input("Модель: ")
                body = input("Тип кузова: ")
                color = input("Цвет: ")
                gear = input("Привод (1. Передний / 2. Задний / 3. Полный): ")
                headlights = input("Состояние фар (1. Включены / 2. Выключены): ")
                doors = input("Состояние дверей (1. Открыты / 2. Закрыты): ")
                engine = input("Состояние двигателя (1. Заведен / 2. Заглушен): ")

                car.brand = brand
                car.model = model
                car.body = body
                car.color = color
                car.gear = gear
                car.headlights = headlights
                car.doors = doors
                car.engine = engine

                print(f"Автомобиль с гос. номером {plate} успешно обновлен.")
                return

        print(f"Автомобиль с гос. номером {plate} не найден.")

    def save_to_file(self):
        with open("auto.txt", "w") as file:
            car_list = [vars(car) for car in self.cars]
            json.dump(car_list, file)

    def load_from_file(self):
        try:
            with open("auto.txt", "r") as file:
                car_list = json.load(file)
                self.cars = [Car(**car_info) for car_info in car_list]
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    car_manager = CarManager()
    car_manager.load_from_file()

    while True:
        print('"Автомобили"')
        print('Меню:\n1. Добавить автомобиль \n2. Удалить автомобиль \
        \n3. Показать список автомобилей \n4. Найти автомобиль в списке \
        \n5. Обновить информацию об автомобиле \n6. Выйти из программы')

        menu = input("Введите номер действия (1-6): ")

        if menu == "1":
            brand = input("Марка: ")
            model = input("Модель: ")
            body = input("Тип кузова: ")
            color = input("Цвет: ")
            plate = input("Гос. номер: ")
            gear = input("Привод (1. Передний / 2. Задний / 3. Полный): ")
            headlights = input("Состояние фар (1. Включены / 2. Выключены): ")
            doors = input("Состояние дверей (1. Открыты / 2. Закрыты): ")
            engine = input("Состояние двигателя (1. Заведен / 2. Заглушен): ")

            new_car = Car(brand, model, body, color, plate, gear, headlights, doors, engine)
            car_manager.add_car(new_car)

        elif menu == "2":
            plate = input("Введите гос. номер для удаления автомобиля: ")
            car_manager.remove_car(plate)

        elif menu == "3":
            car_manager.display_cars()

        elif menu == "4":
            plate = input("Введите гос. номер для поиска автомобиля: ")
            car_manager.find_car(plate)

        elif menu == "5":
            plate = input("Введите гос. номер для обновления информации об автомобиле: ")
            car_manager.update_car(plate)

        elif menu == "6":
            car_manager.save_to_file()
            print("До свидания!.")
            break

        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 6.")

        more_actions = input("\nХотите выполнить еще действия? (1. Да / 2. Нет): ")
        if more_actions != "1":
            car_manager.save_to_file()
            print("До свидания!")
            break