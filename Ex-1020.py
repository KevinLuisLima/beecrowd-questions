def transformTotalDaysLivedIntoYearsMonthsAndDays(daysLived):
    timeLoop = True
    timeComplete = [0,0,0]
    while timeLoop != False:
        if daysLived >= 365:
            timeComplete[2] += 1
            daysLived -= 365
        elif daysLived >= 30:
            timeComplete[1] += 1
            daysLived -= 30
        elif daysLived >= 1:
            timeComplete[0] += 1
            daysLived -= 1
        else:
            timeLoop = False
    return timeComplete

daysLived = int(input())
timeComplete = transformTotalDaysLivedIntoYearsMonthsAndDays(daysLived)
print(f"{timeComplete[2]} ano(s)\n{timeComplete[1]} mes(es)\n{timeComplete[0]} dia(s)")