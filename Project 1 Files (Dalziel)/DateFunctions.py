# Libraries

import datetime


def CurrentDay():
    # Displays the current date - Month DD YYYY

    currDate = datetime.datetime.today()
    currDate = datetime.datetime.strftime(currDate, "%B %d, %Y")

    return currDate



def FirstDayNextMonth():
    # Display the first day of the next month (from the current day). Month DD, YYYY


    currDate = datetime.datetime.today()

    day = currDate.day
    month = currDate.month
    year = currDate.year

    if month == 12:
        firstDayNextMonth = datetime.date((year + 1), ((month - month) + 1), ((day - day) + 1))

    else:
        firstDayNextMonth = datetime.date(year, (month + 1), ((day-day) + 1))


    firstDayNextMonth = datetime.datetime.strftime(firstDayNextMonth, "%B %d, %Y")


    return firstDayNextMonth







