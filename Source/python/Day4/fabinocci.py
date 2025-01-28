def fabinocci(n):
    if n<=0:
        return "Enter a positive number"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fabinocci(n-1)+fabinocci(n-2)
def main():
    n=int(input("Enter the number of elements:"))
    for i in range(1,n+1):
        print(fabinocci(i),end=" ")
main()
