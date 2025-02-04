import queue
import threading
import time
q=queue.Queue()
def producer():
    for i in range(5):
        q.put(i)
        print("Produced",i)
        time.sleep(1)
def consumer():
    for i in range(5):
        print("Consumed",q.get())
        time.sleep(1)
thread1=threading.Thread(target=producer)
thread2=threading.Thread(target=consumer)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Main thread execution completed.")