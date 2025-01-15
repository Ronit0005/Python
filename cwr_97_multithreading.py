'''import threading
import time
def func(seconds):
    print(f'Sleept for {seconds}')
    time.sleep(seconds)
    return seconds
t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[3])
t3=threading.Thread(target=func,args=[2])
time1=time.perf_counter()
t1.start()
t2.start()
t3.start()
t1.join()
print(time.perf_counter()-time1)'''
'''from concurrent.futures import ThreadPoolExecutor
import time
import threading
def func(seconds):
    print(f'Sleept for {seconds}')
    time.sleep(seconds)
    return seconds
def pool():
    with ThreadPoolExecutor() as executor:
        future1=executor.submit(func,4)
        future2=executor.submit(func,3)
        future3=executor.submit(func,2)
        print(future1.result())
        print(future2.result())
        print(future3.result())
pool()'''                                                                                                                                                                                                                                                                                                                                                                                                                           
'''from concurrent.futures import ThreadPoolExecutor
import time
def func(seconds):
    print(f'Sleept for {seconds}')
    time.sleep(seconds)
    return seconds
def poolTest():
    with ThreadPoolExecutor() as executor:
        list=[1,2,3,4,5]
        results=executor.map(func,list)
        for result in results:
            print(result)
poolTest()'''