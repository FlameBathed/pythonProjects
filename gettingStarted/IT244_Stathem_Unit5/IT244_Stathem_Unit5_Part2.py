recordsList = []
countRecord = 0
with open("IT244_U5_Data.txt", "r", encoding='cp1252') as fp:
    for line in fp:
        recordsList.append(line.strip())
recordsList.append("5,Brady,Bobby,4222 Clinton Way,Los Angeles,CA")
csvFile =  open("IT244_U5_PromoCredit.csv", 'w', encoding='cp1252')
csvFile.write("Customer ID, Last Name, First Name, Address, City, State, Promo Credit\n")
with open("IT244_U5_PromoCredit.csv", 'a', encoding='cp1252') as csvFile:
    for element in recordsList:
        csvFile.write(recordsList[countRecord] + ",$500\n")
        countRecord = countRecord+1
print("There were " + str(countRecord) + " records written to the IT244_U5_PromoCredit.csv file.")