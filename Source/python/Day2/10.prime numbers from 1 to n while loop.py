import math
def isprime(n):
    if n==1:
        return False
    i=2
    while(i<=math.sqrt(n)):
        if n%i==0:
            return False
        i+=1
    return True
def main():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    if (a>b):
        print("Enter a valid range")
        return
    if(a<0 or b<0):
        print("Enter a positive number")
        return
    itr=a
    while(itr<=b):
        if isprime(itr):
            print(itr,end=" ")
        itr+=1
main()