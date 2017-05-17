"""
NAME: WEIKAMA TITUS
STUDENT NUMBER: 216003567
REG NUMBER: 16/U/12387/PS
COURSE: BSc COMPUTER ENGINEERING
"""

import calendar
print(" THIS PROGRAM IS INTENDED TO DETERMINE THE DAY YOU WERE BORN")

DAY= MONTH = YEAR = None

while(DAY == None):
    try:
        DAY = int(input("Please type in your day: "))
        while( DAY not in range(1, 32)):
            print("this is not a day")
            DAY = int(input("Please type in your day: "))

    except:
        print("Please type in numbers only others exit if you are a NEWBIE")
        print()

while(MONTH == None):
    try:
        MONTH = int(input("Please type in your month: "))
        while(MONTH not in range(1, 13)):
            print("Mr or Lady, months move from Jan, To December. thats twelve, not %d or whatever you've input" % MONTH)
            MONTH = int(input("Please type in your MONTH AGAIN: "))

    except:
        print("Please type in numbers only")
        print()

while(YEAR == None):
    try:
        YEAR = int(input("Please type in your year: "))
        while(YEAR not in range(1000, 2500)):
            if(YEAR >= 2500):
                print("No offense but by %d, you'll be dead, ALREADY. So please, type in " % YEAR)
                YEAR = int(input("Please type in your year: "))
            if(YEAR < 1000):
                print("By then you were not born. Unless you are immortal")
                YEAR = int(input("Please type in your year: "))

    except:
        print("Please type in numbers only")
        print()

dte = calendar.weekday(DAY, MONTH, DAY)
exact = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("You were born on ", exact[dte])


input("press Enter to exit")
