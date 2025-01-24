import math
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def main(): 
    a=int(input("Enter the lower bound number:"))
    b=int(input("Enter the upper bound number:"))
    if (a>b):
        print("Enter a valid range")
        return
    if(a<0 or b<0):
        print("Enter a positive number")
        return
    for i in range(a,b+1):
        if is_prime(i):
            print(i,end=" ")
main()





