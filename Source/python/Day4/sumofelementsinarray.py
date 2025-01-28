n=int(input("Enter the no.of Elements to be added: "))
print(f"Enter {n} values")
l9=[]
for i in range(1,n+1):    
    ans=int(input(f"Enter the element {i}: "))
    l9.append(ans)
sum=0
for i in l9:
    sum+=i
print(f"Sum of Integers in list is : {sum}")

# numbers=[int(input(f"Enter number {i+1}:")) for i in range(5)]
