#Prompt for input
def askForMiles():
    userM = input(f"Please enter the distance in M: ")
    return float(userM)
#converting input and rounding to nearest thousandths place
def convertToKilometers(userM):
    KM = userM/0.62137
    return round(KM, 3)