# grade 
name = input("ENTER UR NAME : ")
a=eval(input("Enter the mark_1 : "))
b=eval(input("Enter the mark_2 : "))
c=eval(input("Enter the mark_3 : "))
d=eval(input("Enter the mark_4 : "))
e=eval(input("Enter the mark_5 : "))

add=(a+b+c+d+e)/500
total=add*100

print()
print(f"NAME \t\t\t: {name}")
print(f"TOTAL MARKS / 500 \t: {total}")
if total>=90:
    print("GRADE \t\t\t: A GRADE")
elif total>=80:
    print("GRADE \t\t\t: B GRADE")
elif total>=70:
    print("GRADE \t\t\t: C GRADE")
elif total>=60:
    print("GRADE \t\t\t: D GRADE")
else:
    print("GRADE \t\t\t: FAILED !!")
print()   