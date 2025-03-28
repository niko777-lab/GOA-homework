# How good are you really?
def better_than_average(class_points, your_points):
    return your_points > (sum(class_points) / len(class_points))

# Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    if not arr:  
        return []
    
    positives = sum(1 for x in arr if x > 0)  # დადებითების რაოდენობა
    negatives = sum(x for x in arr if x < 0)  # უარყოფითების ჯამი
    
    return [positives, negatives]
# DNA to RNA Conversion
def dna_to_rna(dna):
    return dna.replace("T", "U")

# Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump
# Calculate BMI
def bmi(weight, height):
    value = weight / (height ** 2)
    if value <= 18.5:
        return "Underweight"
    elif value <= 25.0:
        return "Normal"
    elif value <= 30.0:
        return "Overweight"
    else:
        return "Obese"
