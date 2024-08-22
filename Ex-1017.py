def totalLitersSpent(hours,distance):
    totalKilometers = hours * distance
    return totalKilometers / 12

hours = float(input())
distance = float(input())
result = totalLitersSpent(hours, distance)
print(f"{result:.3f}")