# Money Calculator

I made this program  because a'lot of people i know have a hard time figuring
out how much they will make in a month and how long until they reach that goal.

So why not share it with others who may have a friend in the same boat?
```bash
T1 = w1 - (tax/2 + gas/2 + bills/4)
T2 = w2-(tax + gas + bills/2)
MT = M-(tax * 2 + gas * 2 + bills)
YT = Y-((tax * 2 + gas * 2 + bills) * 12)
```

So although this may look confusing i did try my best to orginize it. But i did do all the math so you wouldn't have to.

```bash
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

```

Train reck i know but once you through in the numbers most of the time it should even itself out to be more readable