def judgingNumbers(A,B,C,D):
    if B > C:
        if D > A:
            if (C + D) > (A + B):
                if C >= 0:
                    if D >= 0:
                        testingIfEven = (A%2)
                        if testingIfEven == 0:
                            return "Valores aceitos"
    
    return "Valores nao aceitos"

inputString = input()
inputString = inputString.split()
A = int(inputString[0])
B = int(inputString[1])
C = int(inputString[2])
D = int(inputString[3])
result = judgingNumbers(A,B,C,D)
print(result)