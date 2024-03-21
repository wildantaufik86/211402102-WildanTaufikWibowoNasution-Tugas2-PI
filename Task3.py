# Write a class that calculates and stores the height and weight of a person in metric. The BMI is calculated using this formula:
# Weight/Height ^ 2 - weight is in kilograms and height is in meters.
# The class should have two properties named:
# Weight
# Height
# The class should have one method that returns a decimal named (no arguments should be accepted): BMI_Value.


class BMI_Calculator:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def BMI_Value(self):
        return self.weight / (self.height ** 2)

# Example usage
person = BMI_Calculator(70, 1.75)  # Weight in kg, Height in meters
print(person.BMI_Value())
