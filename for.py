l=[]
a = eval(input("ENTER THE LIMIT : "))

for x in range(1,a+1):
    name = input(f"ENTER THE NBR {x} : ")
    l.append(name)

print(f"THE LIST CONTAINS : {l}")