def Main(A,B,C):
    A_grade = A * 2
    B_grade = B * 3
    C_grade = C * 5
    result = (A_grade + B_grade + C_grade)/10
    return result


A = float(input())
B = float(input())
C = float(input())
result = Main(A,B,C)
print(f"MEDIA = {result:.1f}")