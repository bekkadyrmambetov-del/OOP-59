# class Transport:
#     def __init__(self, speed):
#         self.speed = speed
#
#     def move(self):
#         return f"Транспорт движется со скоростью {self.speed} км/ч"
#
#
# class Honda(Transport):
#     def __init__(self, speed, brand):
#         super().__init__(speed)
#         self.brand = brand
#
#     def move(self):
#         return f"Машина {self.brand} едет со скоростью {self.speed} км/ч"
#
# car = Honda(120, "BMW")
#
# print(car.move())