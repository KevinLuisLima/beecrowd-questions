def calculateAverage(firstGrade, secondGrade, thirdGrade, fourthGrade):
    A_grade = firstGrade * 2
    B_grade = secondGrade * 3
    C_grade = thirdGrade * 4
    D_grade = fourthGrade * 1
    return ((A_grade + B_grade + C_grade + D_grade) / 9)

def finalChance(average,finalGrade):
    return ((average + finalGrade) / 2)

inputString = input()
inputString = inputString.split()
firstGrade = float(inputString[0])
secondGrade = float(inputString[1])
thirdGrade = float(inputString[2])
fourthGrade = float(inputString[3])

average = calculateAverage(firstGrade, secondGrade, thirdGrade, fourthGrade)
print(f"Media: {average:.1f}")
if average >= 7:
    print(f"Aluno aprovado.")
elif average >= 5:
    print("Aluno em exame.")
    finalGrade = float(input())
    print(f"Nota do exame: {finalGrade:.1f}")
    finalAverage = finalChance(average, finalGrade)
    if finalAverage >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {finalAverage:.1f}")
else:
    print("Aluno reprovado.")