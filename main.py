from os import system

# Title
print("             Money Calculator")

# Questions being asked
pay = int(input("pay: >>>"))
hrs = int(input("hrs: >>>"))
gas = int(input("gas per week?: >>>"))
bills = int(input("bill's per month?: >>>"))
tax = int(input("tax's per bi weekly?: >>>"))
goal = int(input("Goal per Year?: >>>").replace(',', ''))

# --Quick if you are tired of questions--
# pay = 10
# hrs = 500
# gas = 120
# bills = 500
# tax = 100
# goal = 1,000,000

# Pay x hourly // This is Calculations for how much your paid
w1 = pay * hrs
w2 = (hrs * 2) * pay
M = ((hrs * 2) * 2) * pay
Y = (((hrs * 2) * 2) * 12) * pay

# This is your pay minus your tax's, gas and bills,
T1 = w1 - (tax/2 + gas/2 + bills/4)
T2 = w2-(tax + gas + bills/2)
MT = M-(tax * 2 + gas * 2 + bills)
YT = Y-((tax * 2 + gas * 2 + bills) * 12)

# This is your goal and how many years until you reach that goal
GT = round(goal/YT, 1)

# Clears Screen
system("cls")

# This is all the Calculations and math solved for you so you can get a
# rough estimate of how much is in your pocket

print(f"             Money Calculator  | ${pay}   {hrs}hrs")
print("______________________________________________")
print("Before tax/etc       |           After tax/etc")
print("______________________________________________")
print(f'Week1: {w1:,}           |           Week1: {T1:,}')
print(f'Week2: {w2:,}           |          Week2: {T2:,}')
print(f'Month: {M:,}         |           Month: {MT:,}')
print(f'Year: {Y:,}         |           Year: {YT:,}')
print("______________________________________________")
print(f"Goal: {goal:,}         |           Goal: {GT:,}yrs")
input("Press Enter To ShutDown...")
