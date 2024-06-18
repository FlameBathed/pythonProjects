def convertTemp(temps,scale):
    if scale == "F":
         temps[1] = (userTemp - 32)* 5/9
         print(f"You entered {userTemp} degrees {scale}. \n The temperature in Fahrenheit is {temps[0]}.\n The temperature in Celsius is {temps[1]}.")
    elif scale == "C":
         temps[0] = userTemp*9/5 + 32
         print(f"You entered {userTemp} degrees {scale}. \n The temperature in Celsius is {temps[1]}.\n The temperature in Fahrenheit is {temps[0]}.")
    return temps
temps = [0, 0]
userTemp = float(input("Please enter the temperature: "))
scale = input("Please enter a single letter to indicate the temperature scale (C or F): ").upper()
if scale == "F":
    temps[0] = userTemp
elif scale == "C":
    temps[1] = userTemp
convertTemp(temps, scale)

