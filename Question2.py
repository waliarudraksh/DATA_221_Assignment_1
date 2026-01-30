def string_info(listOfStrings):
    resultDictionary = {}
    # Go through each string in the list
    for currentString in listOfStrings:
        stringLength = len(currentString)
        lengthParity = "even" if stringLength % 2 == 0 else "odd"
        # Store the length and whether it is even or odd
        resultDictionary[currentString] = {
            "length": stringLength,
            "parity": lengthParity
        }
    return resultDictionary