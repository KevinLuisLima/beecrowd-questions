def summaryOfItensCalculator(firstItenTotal, firstItenPrice, secondItenTotal, secondItenPrice):
    firstSummary = firstItenTotal * firstItenPrice
    secondSummary = secondItenTotal * secondItenPrice
    return (firstSummary + secondSummary)

repeat = True
firstItenIndex = "none"
while repeat:
    inputString = input()
    inputString = inputString.split()

    if(firstItenIndex == "none"):
        firstItenIndex = int(inputString[0])
        firstItenTotal = float(inputString[1])
        firstItenPrice = float(inputString[2])
    else:
        secondItenTotal = float(inputString[1])
        secondItenPrice = float(inputString[2])
        result = summaryOfItensCalculator(firstItenTotal, firstItenPrice, secondItenTotal, secondItenPrice)
        print(f"VALOR A PAGAR: R$ {result:.2f}")
        repeat = False