def bonusCalculator(salary, sellings):
    bonus = ((sellings * 15)/100)
    return (bonus + salary)

name = input()
salary = float(input())
sellings = float(input())
result = bonusCalculator(salary,sellings)
print(f"TOTAL = R$ {result:.2f}")