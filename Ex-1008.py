def monthlySalary(workedHours,salaryPerHour):
    return workedHours * salaryPerHour

number = input()
workedHours = float(input())
salaryPerHour = float(input())
print(f"NUMBER = {number}")
result = float(monthlySalary(workedHours,salaryPerHour))
print(f"SALARY = U$ {result:.2f}")