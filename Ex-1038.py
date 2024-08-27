def calculateTotalForSnack(code, quantity):
    if code == 1:
        multiplier = 4
    elif code == 2:
        multiplier = 4.5
    elif code == 3:
        multiplier = 5
    elif code == 4:
        multiplier = 2
    elif code == 5:
        multiplier = 1.5
    
    return quantity * multiplier

inputString = input()
inputString = inputString.split()
code = int(inputString[0])
quantity = int(inputString[1])
result = calculateTotalForSnack(code,quantity)
print(f"Total: R$ {result:.2f}")