#prompt for input
def askForKilometers():
    userKM = input(f"Please enter the distance in KM: ")
    return float(userKM)
#converting input and rounding to nearest thousandths place
def convertToMiles(userKM):
    M = userKM * 0.62137
    return round(M, 3)
