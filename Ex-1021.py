def calculateBankNotes(totalMoney):
    moneyIndex = totalMoney
    typeOfBankNotes = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
    loopIndex = True
    while loopIndex != False:
        if moneyIndex >= 100:
            typeOfBankNotes[11] += 1
            moneyIndex -= 100
        elif moneyIndex >= 50:
            typeOfBankNotes[10] += 1
            moneyIndex -= 50
        elif moneyIndex >= 20:
            typeOfBankNotes[9] += 1
            moneyIndex -= 20
        elif moneyIndex >= 10:
            typeOfBankNotes[8] += 1
            moneyIndex -= 10
        elif moneyIndex >= 5:
            typeOfBankNotes[7] += 1
            moneyIndex -= 5
        elif moneyIndex >= 2:
            typeOfBankNotes[6] += 1
            moneyIndex -= 2

        elif moneyIndex >= 1:
            typeOfBankNotes[5] += 1
            moneyIndex -= 1
        elif moneyIndex >= 0.5:
            typeOfBankNotes[4] += 1
            moneyIndex -= 0.5
        elif moneyIndex >= 0.25:
            typeOfBankNotes[3] += 1
            moneyIndex -= 0.25
        elif moneyIndex >= 0.1:
            typeOfBankNotes[2] += 1
            moneyIndex -= 0.1
        elif moneyIndex >= 0.05:
            typeOfBankNotes[1] += 1
            moneyIndex -= 0.05
        elif moneyIndex >= 0.001:
            typeOfBankNotes[0] += 1
            moneyIndex -= 0.01
        else:
            loopIndex = False
    return typeOfBankNotes

baseTypeOfBankNotes = ([0.01, 0.05, 0.10, 0.25, 0.50, 1.00, 2.00, 5.00, 10.00, 20.00, 50.00, 100.00])
totalMoney = float(input())
typeOfBankNotes = calculateBankNotes(totalMoney)
loopIndex = 12
while loopIndex != 0:
    if loopIndex == 12:
        print("NOTAS:")
    if loopIndex >= 7:
        print(f"{typeOfBankNotes[loopIndex-1]:.0f} nota(s) de R$ {baseTypeOfBankNotes[loopIndex-1]:.2f}")
    else:
        if loopIndex == 6:
            print("MOEDAS:")
            print(f"{typeOfBankNotes[loopIndex-1]:.0f} moeda(s) de R$ {baseTypeOfBankNotes[loopIndex-1]:.2f}")
        else:
            print(f"{typeOfBankNotes[loopIndex-1]:.0f} moeda(s) de R$ {baseTypeOfBankNotes[loopIndex-1]:.2f}")
    loopIndex -= 1