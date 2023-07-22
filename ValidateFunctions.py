# Libraries:

import datetime


def ProvVal(request):
    # Validates a Canadian province (2 letter abbreviation)

    ProvLst = ["NL", "NS", "PE", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
    while True:
        prov = input(f"{request}").upper()
        if prov not in ProvLst:
            print("Error - please re-enter using a valid two-letter abbreviation (ex. NL).")
        else:
            break

    return prov


def PostCode(request):
    # Validates a Canadian postal code

    while True:
        postCode = input(f"{request}").upper()
        if postCode == "":
            print("Error - postal code cannot be blank.")
        elif len(postCode) != 6:
            print("Error - postal code must be 6 characters long. Please re-enter.")
        elif postCode[0].isalpha() == False:
            print("Error - please make sure you enter letters/numbers only using the format A1A1A1.")
        elif postCode[2].isalpha() == False:
            print("Error - please make sure you enter letters/numbers only using the format A1A1A1.")
        elif postCode[4].isalpha() == False:
            print("Error - please make sure you enter letters/numbers only using the format A1A1A1.")
        elif postCode[1].isdigit() == False:
            print("Error - please make sure you enter letters/numbers only using the format A1A1A1.")
        elif postCode[3].isdigit() == False:
            print("Error - please make sure you enter letters/numbers only using the format A1A1A1.")
        elif postCode[5].isdigit() == False:
            print("Error - please make sure you enter letters/numbers only using the format A1A1A1.")
        else:
            break

    return postCode


def SevenPhNum():
    # Validates a seven-digit phone number (no area code)

    while True:
        phNum = input("Enter the phone number (1112222): ")
        if phNum == "":
            print("Error - the phone number cannot be blank.")
        elif phNum.isdigit() == False:
            print("Error - the phone number can only contain numbers. Please re-enter.")
        elif len(phNum) != 7:
            print("Error - phone number must contain 7 digits. Please re-enter.")
        else:
            break

    return phNum


def TenPhNum(request):
    # Validates a ten-digit phone number (includes area code).

    while True:
        phNum = input(f"{request}")
        if phNum == "":
            print("Error - the phone number cannot be blank.")
        elif phNum.isdigit() == False:
            print("Error - the phone number can only contain numbers. Please re-enter.")
        elif len(phNum) != 10:
            print("Error - phone number must contain 10 digits. Please re-enter.")
        else:
            break

    return phNum


def YYYYMMDDDate(DateInput):
    # Validates a date using format YYYY-MM-DD.

    while True:
        date = input(f"Enter the {DateInput}:")
        try:
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
        except:
            print("Error - invalid entry. Please re-enter using the format YYYY-MM-DD.")
        else:
            break

    return date.date()

