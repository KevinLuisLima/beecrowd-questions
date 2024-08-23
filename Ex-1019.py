def transformTimeInSecondsToComplete(timeInSeconds):
    timeLoop = True
    timeComplete = [0,0,0]
    while timeLoop != False:
        if timeInSeconds >= 3600:
            timeComplete[2] += 1
            timeInSeconds -= 3600
        elif timeInSeconds >= 60:
            timeComplete[1] += 1
            timeInSeconds -= 60
        elif timeInSeconds >= 1:
            timeComplete[0] += 1
            timeInSeconds -= 1
        else:
            timeLoop = False
    return timeComplete

timeInSeconds = int(input())
timeComplete = transformTimeInSecondsToComplete(timeInSeconds)
print(f"{timeComplete[2]}:{timeComplete[1]}:{timeComplete[0]}")