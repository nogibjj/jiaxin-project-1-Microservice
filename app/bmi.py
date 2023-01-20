from flask import jsonify
from abc import ABC, abstractmethod

class Bmi(ABC):
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    @abstractmethod
    def calculate(self):
        label = ""
        try:
            bmi = round((self.weight/pow((self.height/100),2)),2) 
            if bmi < 18.5:
                label = "You are underweight, please start gaining weight."
            elif 18.5 <= bmi <= 24.9:
                label = "Congratulations, your are healthy!"
            elif bmi >= 25.0:
                label = "You are overweight, please being losing weight."
        except ZeroDivisionError as e:
            return jsonify(error=str(e))

        return jsonify(bmi=bmi, label=label)

class BmiStatus(Bmi):
    def calculate(self):
        if self.weight is None and self.height is None:
            message = "Hi, welcome to come to BMI calculator, please show your weight (kg) and height (cm) to check your health status by typing:/?weight=xx&height=xx"
            return jsonify(message=message)

        result = super().calculate()
        return result