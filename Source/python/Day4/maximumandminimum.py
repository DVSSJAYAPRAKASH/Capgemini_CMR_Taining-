# n=int(input("Enter the no.of Elements to be added: "))
# print(f"Enter {n} values")
# lista=[]
# maxi=float('-inf')
# mini=float('inf')
# for i in range(1,n+1):
#     ans=int(input(f"Enter the element {i}: "))
#     lista.append(ans)
# for i in lista:
#      if i>maxi:
#         maxi=i
#      if mini>i:
#         mini=i
# print("Maximum Element in array: ",maxi)
# print("Minimum Element in array :",mini)

def get_input():
    nums = [int(input(f"Enter number {i+1}:")) for i in range((int(input("Enter the size of nums:"))))]
    return nums

def maxandmin(nums):
    global small,big
    small = float('inf')
    big = float('-inf')
    for i in range(len(nums)):
        if nums[i] < small:
            small = nums[i]
        if nums[i] > big:
            big = nums[i]
    return small,big

def main():
    global small,big
    nums = get_input()
    maxandmin(nums)
    print("Smallest Number:", small)
    print("Biggest Number:", big)

main()
