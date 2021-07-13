from temperature import Temperature


class Calorie:
    def __init__(self, weight, height, age, temperature):
        self.height = height
        self.weight = weight
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
        return result


if __name__ == "__main__":
    temperature = Temperature("Italy", "Rome").get()
    calorie = Calorie(70, 175, 32, temperature)
    print(calorie.calculate())

