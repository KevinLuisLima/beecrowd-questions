def findInterval(number):
    if number >= 0:
        if number > 25:
            if number > 50:
                if number > 75:
                    if number > 100:
                        return "Fora de intervalo"
                    else:
                        return "(75,100]"
                else:
                    return "(50,75]"
            else:
                return "(25,50]"
        else:
            return "[0,25]"
    else:
        return "Fora de intervalo"
    
number = float(input())
result = findInterval(number)
if result != "Fora de intervalo":
    print(f"Intervalo {result}")
else: print("Fora de intervalo")