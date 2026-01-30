import pandas as pd
# Create the data for the DataFrame
data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}
# Create the DataFrame
dataFrame = pd.DataFrame(data)
# Add a new column based on existing columns
dataFrame["D"] = dataFrame["A"] * dataFrame["B"]
# Print the final DataFrame
print(dataFrame)