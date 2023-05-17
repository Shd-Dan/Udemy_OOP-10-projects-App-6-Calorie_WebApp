class Calorie:
    """Represents optimal calorie amount a person needs to take today"""

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.temperature = temperature

    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
        return result


if __name__ == "__main__":
    pass
