# This program generates a receipt for One Stop Insurance Company's customers.
# Amy Dalziel
# July 17-25, 2023

# Import Libraries

import ValidateFunctions as VF
import FormatValues as FV
import DateFunctions as DF
from tqdm import trange
from time import sleep

# Read data from OSICDef.dat

f = open("OSICDef.dat", "r")

NEXT_POL_NUM = int(f.readline())
BASIC_PREM = float(f.readline())
DIS_RATE_ADD_CARS = float(f.readline())
EXTRA_LIABILITY_COV = float(f.readline())
GLASS_COV = float(f.readline())
LOANER_CAR_COV = float(f.readline())
HST_RATE = float(f.readline())
PROC_FEE_MNTHPAY= float(f.readline())


f.close()

# Inputs (and Validations)

while True:

    while True:
        custFirName = input("Enter the customer's first name: ").title()
        if custFirName == "":
            print("Error - the customer's first name cannot be blank.")
        else:
            break

    while True:
        custLastName = input("Enter the customer's last name: ").title()
        if custLastName == "":
            print("Error - the customer's last name cannot be blank.")
        else:
            break

    while True:
        custStAdd = input("Enter the customer's street address: ").title()
        if custStAdd == "":
            print("Error - the street address cannot be blank.")
        else:
            break

    while True:
        custCity = input("Enter the customer's city: ").title()
        if custCity == "":
            print("Error - the city cannot be blank.")
        else:
            break

    custProv = VF.ProvVal("Enter the customer's province (ex. NL): ")

    custPostCd = VF.PostCode("Enter the customer's postal code (A1A1A1): ")

    custPhNum = VF.TenPhNum("Enter the customer's phone number (1112223333): ")

    while True:
        try:
            numCarInsured = int(input("Enter the number of cars being insured: "))
        except:
            print("Error - the number of cars must be a valid number.")
        else:
            break

    while True:
        extraLiabilityChoice = input("Do you wish to purchase extra liability insurance (up to $1,000,000.00)? Enter Y for YES or N for NO: ").upper()
        if extraLiabilityChoice == "Y" or extraLiabilityChoice== "N":
            break
        else:
            print("Error - please enter Y for YES or N for N.")

    while True:
        glassCoverageChoice = input("Do you wish to purchase glass coverage? Enter Y for YES or N for NO: ").upper()
        if glassCoverageChoice == "Y" or glassCoverageChoice == "N":
            break
        else:
            print("Error - please enter Y for YES or N for N.")

    while True:
        loanerCarChoice = input("Do you wish to purchase the loaner car coverage? Y for YES or N for NO: ").upper()
        if loanerCarChoice == "Y" or loanerCarChoice == "N":
            break
        else:
            print("Error - please enter Y for YES or N for N.")

    paymentLst = ["Full", "Monthly"]
    while True:
        paymentSched = input("Enter your preferred payment schedule (Full / Monthly): ").title()
        if paymentSched not in paymentLst:
            print("Error - please enter Full or Monthly as your preferred payment schedule.")
        else:
            break


# Calculations

    insPrem = 0
    if numCarInsured == 1:
        insPrem = BASIC_PREM
    else:
        insPrem = BASIC_PREM + ((numCarInsured - 1) * (BASIC_PREM - (BASIC_PREM * DIS_RATE_ADD_CARS)))

    extraLiabilityCost = 0
    if extraLiabilityChoice == "Y":
        extraLiabilityCost = EXTRA_LIABILITY_COV * numCarInsured

    glassCoverageCost = 0
    if glassCoverageChoice == "Y":
        glassCoverageCost = GLASS_COV * numCarInsured

    loanerCarCost = 0
    if loanerCarChoice == "Y":
        loanerCarCost = LOANER_CAR_COV * numCarInsured

    totExtraCost = extraLiabilityCost + glassCoverageCost + loanerCarCost

    totInsPrem = insPrem + totExtraCost

    hst = totInsPrem * HST_RATE

    totCost = totInsPrem + hst

    if paymentSched == "Monthly":
        monthPay = (totCost + PROC_FEE_MNTHPAY) / 8


# Output / Receipt

    print()
    print()
    print("                  One Stop Insurance Company")
    print("                      Customer Receipt")
    print()
    print(f"Policy Number: {NEXT_POL_NUM:>5d}                        {DF.CurrentDay():>18s}")
    print("--------------------------------------------------------------")
    print()

    custFullName = custFirName + " " + custLastName
    print(f"{custFullName:<25s}                 No. Cars Insured: {numCarInsured:>2d}")
    print(" "*31, "------------------------------")


    if extraLiabilityChoice == "Y":
        extraLiabilityReceipt = "YES"
    else:
        extraLiabilityReceipt = "NO"

    if glassCoverageChoice == "Y":
        glassCoverageReceipt = "YES"
    else:
        glassCoverageReceipt = "NO"

    if loanerCarChoice == "Y":
        loanerCarReceipt = "YES"
    else:
        loanerCarReceipt = "NO"
    print(f"{custStAdd:<25s}       Extra Liability Insurance: {extraLiabilityReceipt:>3s}")
    moreAddress = custCity + "," + " " + custProv + " " + FV.PostCd(custPostCd)
    print(f"{moreAddress:<25s}       Glass Coverage Insurance:  {glassCoverageReceipt:>3s}")
    print(f"{FV.TenDigitPh(custPhNum):<25s}       Loaner Car Insurance:      {loanerCarReceipt:>3s}")
    print()

    print(f"Insurance Premium................................... {FV.FDollar2(insPrem):>9s}")
    print()
    if extraLiabilityChoice == "Y":
        print(" "*28, f"Extra Liability Charge: {FV.FDollar2(extraLiabilityCost):>9s}")
    if glassCoverageChoice == "Y":
        print(" "*28, f"Glass Coverage Charge:  {FV.FDollar2(glassCoverageCost):>9s}")
    if loanerCarChoice == "Y":
        print(" "*28, f"Loaner Car Charge:      {FV.FDollar2(loanerCarCost):>9s}")

    if totExtraCost != 0:
        print(" "*28, "---------------------------------")
        print(" "*28, f"Total Extra Charges:      {FV.FDollar2(totExtraCost)}")
        print()
        print(f"Total Insurance Premiums............................ {FV.FDollar2(totInsPrem)}")

    print(f"HST................................................... {FV.FDollar2(hst)}")
    print()
    print(f"TOTAL COST.......................................... {FV.FDollar2(totCost)}")
    print()

    if paymentSched == "Full":
        print(f"Payment due in full on {DF.FirstDayNextMonth()}.")
    else:
        print()
        print(f"Payment: 8 monthly installments of {FV.FDollar2(monthPay)}.")
        print()
        print(f"Please submit your first payment by {DF.FirstDayNextMonth()}.")
    print("--------------------------------------------------------------")
    print(f"                Thank you for your service.")
    print()
    print()

# Save and update data files

    print("Please wait while data saves...")
    print()

    for i in trange(60):
        sleep(.1)

    f = open("Policies.dat", "a")

    f.write(f"{NEXT_POL_NUM}, ")
    f.write(f"{DF.CurrentDay()}, ")
    f.write(f"{custFirName}, ")
    f.write(f"{custLastName}, ")
    f.write(f"{custStAdd}, ")
    f.write(f"{custCity}, ")
    f.write(f"{custProv}, ")
    f.write(f"{custPostCd}, ")
    f.write(f"{custPhNum}, ")
    f.write(f"{numCarInsured}, ")
    f.write(f"{extraLiabilityChoice}, ")
    f.write(f"{glassCoverageChoice}, ")
    f.write(f"{loanerCarChoice}, ")
    f.write(f"{paymentSched}, ")
    f.write(f"{totInsPrem}\n ")

    f.close()

    print()
    print("Data has successfully saved...")
    print()

    NEXT_POL_NUM += 1

    f = open("OSICDef.dat", "w")
    f.write(f"{NEXT_POL_NUM}\n")
    f.write(f"{BASIC_PREM}\n")
    f.write(f"{DIS_RATE_ADD_CARS}\n")
    f.write(f"{EXTRA_LIABILITY_COV}\n")
    f.write(f"{GLASS_COV}\n")
    f.write(f"{LOANER_CAR_COV}\n")
    f.write(f"{HST_RATE}\n")
    f.write(f"{PROC_FEE_MNTHPAY}\n")

    f.close()

    while True:
        contLst = ["Y", "N"]
        cont = input("Do you wish to submit another policy? (Y/N): ").upper()
        if cont not in contLst:
            print("Error - please enter Y to submit another policy or N to exit the program.")
        else:
            print()
            break

    if cont == "N":
        print("Thank you for using the One Stop Insurance Company Customer Receipt Program.")
        print("Have a good day.")
        break


