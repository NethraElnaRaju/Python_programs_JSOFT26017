#largest of 3 nbr
a=eval(input("Enter the nbr_1 : "))
b=eval(input("Enter the nbr_2 : "))
c=eval(input("Enter the nbr_3 : "))

if a>b and a>c:
    print(f"THE  NUMBER {a} IS LARGEST")
elif b>a and b>c:
    print(f"THE  NUMBER {b} IS LARGEST")
elif c>a and c>b:
    print(f"THE  NUMBER {c} IS LARGEST")
else:
    print("INVAILD")
    
