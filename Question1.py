threshold = 100
product = 1
currentNumber = 1
# Keep multiplying numbers until the product is bigger than the threshold
while product <= threshold:
    product *= currentNumber
    currentNumber += 1
# Print the result and the number that caused the product to go over the limit
print("Final product:", product)
print("Number that exceeded the threshold:", currentNumber - 1)