import math
a=int(input("Enter a value number:"))
b=int(input("Enter b value number:"))
c=int(input("Enter c value number:"))

print("Roots of a quadratic equation are:")
d=b*b-4*a*c
root1=(-b+math.sqrt(d))//(2*a)
root2=(-b-math.sqrt(d))//(2*a)
print(f"Root1={root1} and Root2={root2}")
