def isprime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def main(): 
    n=int(input("Enter the number:"))
    if isprime(n):
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")
main()
    