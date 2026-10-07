#prime nbr / not 

a=eval(input("ENTER THE NBR : "))
print()
for x in range(2,a):
    if a%x==0:
        print(f"~THE NBR {a} IS NOT PRIME NBR~")
        break
else:
    print(f"~THE NBR {a} IS A PRIME NBR~")   

print() 

