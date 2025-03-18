def getHeightInMeters(heightFeet, heightInches):
    ftToInches = heightFeet * 12
    totalInches = ftToInches + heightInches
    return totalInches * 0.025

def getBmi(heightFeet, heightInches, weightLbs):
    kgWeight = weightLbs * .45
    meterHeight = getHeightInMeters(heightFeet, heightInches)
    heightSquared = meterHeight * meterHeight
    return round((kgWeight / heightSquared), 1)

def getBmiCategory(BMI):
    if BMI < 18.5:
        return "Underweight"
    elif BMI < 25:
        return "Normal Weight"
    elif BMI < 30:
        return "Overweight"
    else:
        return "Obese"
    
print("Welcome to BMI calculator")
heightFeet, heightInches = input("Enter height in feet then inches: ").split()
weightLbs = float(input("Enter weight in lbs: "))

print("BMI: ", getBmi(float(heightFeet), float(heightInches), weightLbs))
print("Category: ", getBmiCategory(getBmi(float(heightFeet), float(heightInches), weightLbs)))


