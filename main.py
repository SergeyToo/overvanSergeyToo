class Car:
    def __init__(self, name, year_of_issue, mileage):
        self.name = name
        self.year_of_issue = year_of_issue
        self.mileage = mileage

    def is_adult(self):
        return self.year_of_issue > 2000


car1 = Car('Lamborghini', 2020, 10000)
car2 = Car('Запорожец', 1977, 10000000)
print(car1.name, car1.year_of_issue, car1.mileage)
print(car2.name, car2.year_of_issue, car2.mileage)

print(car2.is_adult())
