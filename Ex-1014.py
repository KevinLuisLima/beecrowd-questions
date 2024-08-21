def litersConsumedPerKilometer(kilometers,liters):
    return kilometers / liters

kilometers = float(input())
liters = float(input())
result = litersConsumedPerKilometer(kilometers, liters)
print(f"{result:.3f} km/l")