import math
def isprime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def take_input():
    st=int(input("Enter the start value : "))
    end=int(input("Enter the end value: "))
    while(st>end):
        print("You Entered a Invalid Range !")
        st=int(input("Enter the start value : "))
        end=int(input("Enter the end value: "))
    return (st,end)
def maxandminprime(st,end):
    list_a=[]
    for i in range(st,end+1):
        if isprime(i):
            list_a.append(i)
    big=float('-inf')
    small=float('inf')
    for i in list_a:
        if big<i:
            big=i
        if small>i:
            small=i
    if small==float('inf'):
        print(f"There is No Smallest Prime is There in between {st} and {end}!")
    else:
        print(f"Smallest Prime is: {small}.")
    if big==float('-inf'):
        print(f"There is No Largest Prime in between {st} and {end}!")
    else:
        print(f"Largest prime is: {big}.")
def main():
    start,end=take_input()
    maxandminprime(start,end)
main()
    

