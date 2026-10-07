year = eval(input("ENTER THE YEAR : "))
if year%4==0:
    if year%400 == 0 or year % 100 !=0:
        print("ITS A LEAP YEAR")
    else:
        print("NOT LEAP YEAR")
else:
    print("NOT LEAP")