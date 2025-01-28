def take_input():
    str=input("Enter the String: ")
    return list(str)
def ispalindrome():
    list_a=take_input()
    for i in range(len(list_a)//2):
        if list_a[i]!=list_a[len(list_a)-i-1]:
            return False
    return True
def main():
    if ispalindrome():
        print("It is a Palindrome!!")
    else:
        print("It is not a Palindrome!!")
main()


