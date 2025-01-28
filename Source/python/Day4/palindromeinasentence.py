def ispalindrome(string):
    return string==string[::-1]

def calculate(list_a):
    cnt=0
    for i in list_a:
        if ispalindrome(i):
            cnt+=1
    return cnt

def take_input():
    string=input("Enter the String: ")
    list_a=[]
    ans=""
    for i in range(len(string)):
        if string[i].isalnum():
            ans+=string[i]
        else:
            if len(ans) > 0:
                list_a.append(ans)
            ans=""
            continue
    if len(ans) > 0:
        list_a.append(ans)
    return list_a

def main():
    global cnt
    print(calculate(take_input()))

main()
