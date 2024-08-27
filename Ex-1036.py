def calculateBhaskaraBetweenNumbers(A,B,C):
    delta = ((B ** 2) - 4 * (A * C))
    if delta >= 0 and A != 0:
        B = (B - (2 * B))
        result1 = (((B) + (delta ** (1/2))) / (2 * A))
        result2 = (((B) - (delta ** (1/2))) / (2 * A))
        result = [result1,result2]
        return result
    else:
        return "Impossivel calcular"

inputString = input()
inputString = inputString.split()
A = float(inputString[0])
B = float(inputString[1])
C = float(inputString[2])
result = calculateBhaskaraBetweenNumbers(A,B,C)
if result != "Impossivel calcular":
    print(f"R1 = {result[0]:.5f}")
    print(f"R2 = {result[1]:.5f}")
else:
    print(result)