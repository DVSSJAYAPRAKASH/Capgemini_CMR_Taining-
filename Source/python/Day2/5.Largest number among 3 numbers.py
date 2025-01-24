def take_input():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    c=int(input("Enter the third number:"))
    return (a,b,c)
def largest(a,b,c):
    if a>b and a>c:
        return a
    if b>a and b>c:
        return b
    return c

def main():
    a,b,c=take_input()
    ans=largest(a,b,c)
    print(f"Maximum number among {a},{b},{c} is : {ans}")
   # print(ans)

main()