import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    """
    Converts working hours taken as input in 12 hour format into 24 hour format.
    
    Accepts input of the following styles:
        9:00 AM to 5:00 PM
        9 AM to 5 PM
        9:00 AM to 5 PM
        9 AM to 5:00 PM

    Returns output by converting these inputs into 24 hrs format
    """

    if matches := re.search(r"^(?P<s_hr>\d\d?)(?P<s_min>:\d\d)? (?P<s_time>[AP]M) to (?P<e_hr>\d\d?)(?P<e_min>:\d\d)? (?P<e_time>[AP]M)$", s):

        # Assigning values to variables
        start_hour_12 = int(matches.group("s_hr"))
        end_hour_12 = int(matches.group("e_hr"))

        if matches.group("s_min"):
            start_mins = int(matches.group("s_min").strip(":"))
        else:
            start_mins = 0
        if matches.group("e_min"):
            end_mins = int(matches.group("e_min").strip(":"))
        else:
            end_mins = 0

        start_time_12 = matches.group("s_time")
        end_time_12 = matches.group("e_time")

        # Doing input validation
        if not (start_hour_12 <= 12 and end_hour_12 <= 12 and start_mins < 60 and end_mins < 60):
            raise ValueError

        # Converting start hour into 24 hours format
        if start_time_12 == "AM":
            start_hour_24 = convert_AM(start_hour_12)
        elif start_time_12 == "PM":
            start_hour_24 = convert_PM(start_hour_12)

        # Converting end hour 24 hr format
        if end_time_12 == "AM":
            end_hour_24 = convert_AM(end_hour_12)
        elif end_time_12 == "PM":
            end_hour_24 = convert_PM(end_hour_12)

        # Returning user output
        return f"{start_hour_24:02}:{start_mins:02} to {end_hour_24:02}:{end_mins:02}"

    else:
        raise ValueError


def convert_AM(time):
    return 0 if time == 12 else time


def convert_PM(time):
    return time if time == 12 else (time+12)


if __name__ == "__main__":
    main()
