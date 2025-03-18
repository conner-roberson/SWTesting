
def getBmi(heightFeet, heightInches, weightLbs):
    if(heightFeet < 0 or heightInches < 0 or weightLbs < 0):
        if(heightFeet < 0 or heightInches < 0):
            print("Invalid Height - NO NEGATIVE VALUES")
            heightFeet, heightInches = input("Retry Enter Height: ").split()
        elif(weightLbs < 0):
            print("Invalid Weight - NO NEGATIVE VALUES")
            weightLbs = input("Retry Enter Weight: ")
    kgWeight = weightLbs * .45
    ftToInches = heightFeet * 12
    totalInches = ftToInches + heightInches
    meterHeight = totalInches * 0.025
    heightSquared = meterHeight * meterHeight
    return round((kgWeight / heightSquared), 1)

def getBmiCategory(BMI):
    if BMI < 0:
        return "Something Went Wrong Please Retry"
    elif BMI < 18.4:
        return "Underweight"
    elif BMI < 25:
        return "Normal Weight"
    elif BMI < 30:
        return "Overweight"
    else:
        return "Obese"
    
print("Welcome to BMI calculator")
heightFeet, heightInches = input("Enter height in feet then inches: ").split()
if(heightFeet < 0 or heightInches < 0):
    print("Invalid Height - NO NEGATIVE VALUES")
    heightFeet, heightInches = input("Retry Enter Height: ").split()
weightLbs = float(input("Enter weight in lbs: "))
if(weightLbs < 0):
    print("Invalid Weight - NO NEGATIVE VALUES")
    weightLbs = input("Retry Enter Weight: ")

print("BMI: ", getBmi(float(heightFeet), float(heightInches), weightLbs))
print("Category: ", getBmiCategory(getBmi(float(heightFeet), float(heightInches), weightLbs)))


