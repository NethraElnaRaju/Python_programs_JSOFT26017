#calculater

print()
limit = eval(input("ENTER THE LIMIT : "))
a = eval(input("ENTER THE NBR_1 : "))
b = eval(input("ENTER THE NBR_2 : "))

for x in range(limit):
    ch = input("ENTER (+,-,/,*) : ")
    if ch=='+':
        print()
        print(f"{a} + {b} = {a+b}")
        print()
    elif ch=='-':
        print()
        print(f"{a} - {b} = {a-b}")
        print()
    elif ch=='*':
        print()
        print(f"{a} * {b} = {a*b}")
        print()
    elif ch=='/':
        print()
        print(f"{a} / {b} = {a/b}")
        print()
    else:
        print("INVAILD")