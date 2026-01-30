def convertSecondsSinceMidnight(secondsSinceMidnight):
    # Check that the input is a valid number of seconds in a day
    if (
        not isinstance(secondsSinceMidnight, int)
        or secondsSinceMidnight < 0
        or secondsSinceMidnight >= 86400
    ):
        return "Invalid input"
    # Convert seconds into hours, minutes, and seconds
    hours = secondsSinceMidnight // 3600
    minutes = (secondsSinceMidnight % 3600) // 60
    seconds = secondsSinceMidnight % 60
    # Decide if the time is AM or PM
    period = "AM" if hours < 12 else "PM"
    hours = hours % 12 or 12
    return f"{hours} {minutes} {seconds} {period}"