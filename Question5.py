import math
def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    # Check that both inputs are positive integers
    if (
        not isinstance(radiusOfCircle1, int)
        or not isinstance(radiusOfCircle2, int)
        or radiusOfCircle1 <= 0
        or radiusOfCircle2 <= 0
    ):
        return "Invalid input: radii must be positive integers"
    # Calculate the area of each circle
    areaOfCircle1 = math.pi * radiusOfCircle1 ** 2
    areaOfCircle2 = math.pi * radiusOfCircle2 ** 2
    # Find the smaller and larger areas
    smallerArea = min(areaOfCircle1, areaOfCircle2)
    largerArea = max(areaOfCircle1, areaOfCircle2)
    # Return the percentage of the larger area covered by the smaller one
    return (smallerArea / largerArea) * 100