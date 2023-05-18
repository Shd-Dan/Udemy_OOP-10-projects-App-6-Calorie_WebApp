class Calorie:
    """ Represents amount af calories with
        BMR = 10*weight + 6.25*height - 5*age + 5 - 10*temperature
    """

    def __init__(self, weight, height, age, temperature):
        self.temperature = temperature
        self.age = age
        self.height = height
        self.weight = weight

    def calculate(self):
        result = 10*self.weight + 6.25*self.height + 5*self.age + 5 - 10*self.temperature
        return result