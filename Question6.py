def distributionAnalysis(numberList):
    totalElements = len(numberList)
    resultDictionary = {}
    # Go through each unique number in sorted order
    for currentValue in sorted(set(numberList)):
        # Count how many numbers are less than or equal to the current value
        countLessOrEqual = sum(
            number <= currentValue for number in numberList
        )
        # Store the percentage for this value
        resultDictionary[currentValue] = (countLessOrEqual / totalElements) * 100
    return resultDictionary