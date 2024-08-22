def calculateDistance(p1,p2):
    return ((((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2)) ** (1/2))

inputString = input()
inputString = (inputString.split())
p1 = [float(inputString[0]),float(inputString[1])]
inputString = input()
inputString = (inputString.split())
p2 = [float(inputString[0]),float(inputString[1])]
result = calculateDistance(p1,p2)
print(f"{result:.4f}")