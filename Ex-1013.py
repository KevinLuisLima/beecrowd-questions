def biggerNumberBetweenTwo(A,B):
    return (((A+B) + abs(A-B)) / 2)

inputString = input()
inputString = inputString.split()
A = int(inputString[0])
B = int(inputString[1])
C = int(inputString[2])

result = biggerNumberBetweenTwo(A,B)
result = int(biggerNumberBetweenTwo(result,C))
print(f"{result} eh o maior")