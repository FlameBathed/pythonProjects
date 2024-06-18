flavorList = ['Chocolate','Vanilla','Strawberry','Mango','Dark Chocolate','Cookies & Cream', 'Mint Chocolate']
priceSize = {'S':'$1.75','M':'$2.75','L':'$3:50'}
descrSize = {'S':'Simply Small','M':'Modern Medium','L':'Legendary Large'}
flavorList.append('Chocolate Delight')
flavorList.sort()
print("Welcome to Ice Ice Creamery!\n")
print("Today's " + str(len(flavorList)) + " flavors are: \n")
count = 1
for element in flavorList:
    print("Flavor #: " + str(count) + " "+ element)
    count = int(count) + 1
print("\nOur available sizes are S, M, or L\n")
userFlavor = int(input("Please select a flavor #: "))
userFlavor = userFlavor - 1
userCone = input("Please select a cone size: ").upper()
print("\nYour total is " + priceSize[userCone])
print("Your " + descrSize[userCone] + " cone of " + flavorList[userFlavor] + " will arrive shortly. \n\nThank you for shopping at the Ice Ice Creamery!")
