dayInMonth=lambda x,y:[[31,28,31,30,31,30,31,31,30,31,30,31],[31,29,31,30,31,30,31,31,30,31,30,31]][x%4==0][y-1]

day=1       #1 Jan 1900 was a Monday. day%7==0 is a sunday
day+=366    #How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Sundays=0

for i in range(1901,2001):
    for j in range(1,13):
        Sundays+=day%7==0
        day+=dayInMonth(i,j)

print("Sun:",Sundays)