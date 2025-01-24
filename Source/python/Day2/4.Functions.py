def display(data):
    print(f"The average of 4 numbers is: {data}")

def get_input():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    c=int(input("Enter the third number:"))
    d=int(input("Enter the fourth number:"))
    return (a,b,c,d)
def calculate(a,b,c,d,n):
    return (a+b+c+d)/n
def main():
    print("Hello User!")
    n=int(input("Enter the number of elements:"))
    a,b,c,d=get_input()
    ans=calculate(a,b,c,d,n)
    display(ans)
main()




