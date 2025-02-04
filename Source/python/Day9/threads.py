import threading
import time

print("Main thread Started")

#time.sleep(4)
def even():
    for i in range(10):
        if i%2==0:
            print(i,end=" ")
    print()
    time.sleep(2)
def odd():
    for i in range(10):
        if i%2!=0:
            print(i,end=" ")
    print()
    time.sleep(2)
thread1=threading.Thread(target=even)
thread2=threading.Thread(target=odd)
thread1.start()
thread1.join()
thread2.start()
thread2.join()
#time.sleep()
print("Main thread execution completed.")
