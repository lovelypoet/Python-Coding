# write a program that convert time in 24h format to 12h format
# input : h hours, m minutes
# output : print a sequence of hh:mm AM/PM

try:
    hour = int(input("Enter hour (0-23): "))
    minute = int(input("Enter minute (0-59): "))
except ValueError:
    print("Please enter valid whole numbers.")
else:
    if 0 <= hour <= 23 and 0 <= minute <= 59:
        period = "AM" if hour < 12 else "PM"
        hour_12 = hour % 12 or 12
        print(f"{hour_12:02}:{minute:02} {period}")
    else:
        print("Please enter an hour from 0 to 23 and a minute from 0 to 59.")