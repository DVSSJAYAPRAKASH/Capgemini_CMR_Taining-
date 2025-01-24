def prime(n):
    list=[True for i in range(n+1)]
    for i in range(2,n+1):
        if list[i]==True:
            for j in range(i*i,n+1,i):
                list[j]=False
    return list

def main():
    n=int(input("Enter the number:"))
    ans=prime(n)
    for i in range(2,n+1):
        if ans[i]==True:
            print(i,end=" ")
main()

