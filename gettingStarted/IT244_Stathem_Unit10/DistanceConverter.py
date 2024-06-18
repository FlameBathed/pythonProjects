import Kilometers
import Miles
validValue=True
processing=True

if validValue is True:
    while processing is True:
        userUnit = input("Please select the current unit of measure (KM/M): ").upper()
        if userUnit == "KM":
            userKM = Miles.askForKilometers()
            userM = Miles.convertToMiles(userKM)
            print("Converting " + str(userKM) + " Kilometers, results in " + str(userM) + " Miles.")
            procUser = input("Hit enter if you would like to continue. If you would like to stop press X. ").upper()
            if procUser == "X":
                processing = False
            else:
                processing = True
        elif userUnit == "M":
            userM = Kilometers.askForMiles()
            userKM = Kilometers.convertToKilometers(userM)
            print("Converting " + str(userM) + " miles, results in " + str(userKM) + " Kilometers.")
            procUser = input("Hit enter if you would like to continue. If you would like to stop press X. ").upper()
            if procUser == "X":
                processing = False
            else:
                processing = True
        else:
            print("Error. Please enter an acceptable unit of measure. Use \"KM\" for Kilometers or \"M\" for Miles. ")
            validValue = False
else:
    validValue = True
if processing is False:
    print("Thank you. Have a pleasant day.")