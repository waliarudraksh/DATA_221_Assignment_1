def computePower(baseValue, exponentValue):
    return baseValue ** exponentValue
pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
validResults = []
# Go through each pair of numbers
for baseValue, exponentValue in pairs:
    # Skip the pair if the exponent is negative
    if exponentValue < 0:
        continue
    # Store the result for valid pairs
    validResults.append(computePower(baseValue, exponentValue))
print(validResults)