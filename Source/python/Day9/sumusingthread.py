import threading

def calculate_sum(numbers, result):
    result.append(sum(numbers))

list1 = list(range(1000000000))
list2 = list(range(100000000, 20000000000))
list3 = list(range(2000000, 3000000))

result = []
threads=[]
for data in [list1, list2, list3]:
    thread = threading.Thread(target=calculate_sum, args=(data, result))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

total_sum = sum(result)

print(f"Sum of list1: {result[0]}")
print(f"Sum of list2: {result[1]}")
print(f"Sum of list3: {result[2]}")
print(f"Total sum: {total_sum}")