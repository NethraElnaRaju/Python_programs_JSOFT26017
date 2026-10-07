l=[]
a = eval(input("ENTER THE LIMIT : "))

for x in range(1,a+1):
    fruit = input(f"ENTER NAME OF FRUIT {x} : ")
    l.append(fruit)

print(f"THE LIST CONTAINS : {l}")
print()
if len(l)>=6:
    print(l[5])
    l[1]= 'mango'  
    print(f"UPDATED LIST IS {l}")