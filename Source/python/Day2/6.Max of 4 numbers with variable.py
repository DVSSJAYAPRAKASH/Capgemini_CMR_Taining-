def take_input():
    max_var=0
    variable='a'
    a=int(input("Enter the first number:"))
    max_var=largest(max_var,a)
    if (max_var==a):
        variable='a'
    b=int(input("Enter the second number:"))
    max_var=largest(max_var,b)
    if (max_var==b):
        variable='b'
    c=int(input("Enter the third number:"))
    max_var=largest(max_var,c)
    if (max_var==c):
        variable='c'
    d=int(input("Enter the fourth number:"))
    max_var=largest(max_var,d)
    if (max_var==d):
        variable='d'
    return (a,b,c,d,max_var,variable)
def largest(a,b):
    if a>b:
        return a
    else:
        return b

def main():
    a,b,c,d,max_var,variable=take_input()
    print(f"Maximum number among a,b,c,d is : {max_var}")
    print(f"And the variable is {variable}")
   # print(ans)

main()