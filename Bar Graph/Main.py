# Bar Graph of Sales from the Giraffe Sanctuary's Gift Shop (January - December 2023)
# Amy Dalziel
# July 17-23, 2023

# Libraries

from matplotlib import pyplot as plt
from matplotlib import style


# Inputs and Validations

monthLst = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
salesLst = []
while True:
    for month in monthLst:
        while True:
            try:
                sales = float(input(f"Enter the total sales for {month}: "))
                salesLst.append(sales)
            except:
                print("Error - sales is not a valid number. Please re-enter.")
            else:
                break

    if sum(salesLst) == 0:
        print("Error - total sales for the 2023 year cannot be 0. Please re-enter sales.")
    else:
        break


# Output as a Bar Graph

style.use('ggplot')


x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y = salesLst

fig, ax = plt.subplots()

ax.bar(x, y, align='center', facecolor='gold', edgecolor='brown', linewidth=2)

ax.set_title("'Gir-graph' of Gift Shop Sales (2023)")
ax.set_ylabel("Gift Shop Sales ($)")
ax.set_xlabel("Month (2023)")

ax.set_xticks(x)
ax.set_xticklabels(("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))

plt.show()


