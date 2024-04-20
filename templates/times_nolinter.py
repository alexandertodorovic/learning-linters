from datetime import datetime
import pytz

def get_current_time_in_japan():
    """
    Get the current time in Japan.

    Returns:
        datetime: The current time in Japan.
    """
    japan_tz = pytz.timezone('Asia/Tokyo')
    japan_time = datetime.now(japan_tz)
    return japan_time

def get_current_time_in_germany():
    """
    Get the current time in Germany.

    Returns:
        datetime: The current time in Germany.
    """
    germany_tz = pytz.timezone('Europe/Berlin')
    germany_time = datetime.now(germany_tz)
    return germany_time

def calculate_time_difference():
    """
    Calculate the time difference between Japan and Germany.

    Returns:
        int: The time difference between Japan and Germany.
    """
    japan_time = get_current_time_in_japan()
    germany_time = get_current_time_in_germany()

    # Only consider the hour part of the time
    time_difference_in_hours = japan_time.hour - germany_time.hour

    # If the result is negative, add 24 to get the correct time difference
    if time_difference_in_hours < 0:
        time_difference_in_hours += 24

    return time_difference_in_hours

if __name__ == '__main__':
    print(get_current_time_in_japan())
    print(get_current_time_in_germany())
    print(calculate_time_difference())
