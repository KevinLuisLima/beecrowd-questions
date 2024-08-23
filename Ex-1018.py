def calculateBankNotes(totalMoney):
    moneyIndex = totalMoney
    typeOfBankNotes = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0])
    loopIndex = True
    while loopIndex != False:
        if moneyIndex >= 100:
            typeOfBankNotes[6] += 1
            moneyIndex -= 100
        elif moneyIndex >= 50:
            typeOfBankNotes[5] += 1
            moneyIndex -= 50
        elif moneyIndex >= 20:
            typeOfBankNotes[4] += 1
            moneyIndex -= 20
        elif moneyIndex >= 10:
            typeOfBankNotes[3] += 1
            moneyIndex -= 10
        elif moneyIndex >= 5:
            typeOfBankNotes[2] += 1
            moneyIndex -= 5
        elif moneyIndex >= 2:
            typeOfBankNotes[1] += 1
            moneyIndex -= 2
        elif moneyIndex >= 1:
            typeOfBankNotes[0] += 1
            moneyIndex -= 1
        else:
            loopIndex = False
    return typeOfBankNotes

baseTypeOfBankNotes = ([1.00, 2.00, 5.00, 10.00, 20.00, 50.00, 100.00])
totalMoney = int(input())
typeOfBankNotes = calculateBankNotes(totalMoney)
loopIndex = 7
print(f"{totalMoney}")
while loopIndex != 0:
    print(f"{typeOfBankNotes[loopIndex-1]:.0f} nota(s) de R$ {baseTypeOfBankNotes[loopIndex-1]:.0f},00")
    loopIndex -= 1