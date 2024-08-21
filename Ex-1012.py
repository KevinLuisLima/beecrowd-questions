def operationA(A,C):
    return ((A * C) / 2)
def operationB(C):
    pi = 3.14159
    return (pi * (C ** 2))
def operationC(A,B,C):
    return(((A + B) * C) / 2)
def operationD(B):
    return B ** 2
def operationE(A,B):
    return A * B

inputString = input()
inputString = inputString.split()
A = float(inputString[0])
B = float(inputString[1])
C = float(inputString[2])
result = operationA(A,C)
print(f"TRIANGULO: {result:.3f}")
result = operationB(C)
print(f"CIRCULO: {result:.3f}")
result = operationC(A,B,C)
print(f"TRAPEZIO: {result:.3f}")
result = operationD(B)
print(f"QUADRADO: {result:.3f}")
result = operationE(A,B)
print(f"RETANGULO: {result:.3f}")