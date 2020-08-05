def main():
    car_1 = Car('brasília', 1968, 'yellow', 80)
    car_2 = Car('beatle', 1981, 'black', 95)

    car_1.speed_up(40)
    car_2.speed_up(50)
    car_1.speed_up(80)
    car_1.stop()
    car_2.speed_up(100)

class Car:
    def __init__(self, model, year, color, max_speed):
        self.model = model
        self.year    = year
        self.color    = color
        self.speed = 0
        self.max_speed = max_speed

    def __str__(self):
        if self.speed == 0: # Carro are park, we can see the year
            messenge = (f"{self.color}'s {self.model.capitalize()} {self.year}")
        elif self.speed < self.max_speed:
            messenge = (f"{self.color}'s {self.model.capitalize()} going at {self.speed} Km/h")
        else:
            messenge = (f"{self.color}'s {self.model.capitalize()} toooo faaaaaaaaaaaaaassst!")
        return messenge

    def speed_up(self, new_speed):
        self.speed = new_speed
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        print(self)

    def stop(self):
        self.speed = 0
        print(self)

main()
