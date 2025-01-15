'''import time
def usingWhileLoop():
    i=0
    while i<50000:
       print(i)
       i+=1
def usingForLoop():
    for i in range(50000):
        print(i)
t=time.time()
usingWhileLoop()
x=(time.time()-t)
s=time.time()
usingForLoop()
y=(time.time()-s)
print(f'The time for while to learn {x}')
print(f'The time for for to learn {y}')'''
import time
import win32com.client
# sleep()
'''for i in range(11):
    if i==0:
        continue
    else:
     print(i)
     time.sleep(1)'''
'''speaker=win32com.client.Dispatch("SAPI.SpVoice")
list =['I','will','fuck','mother','of','vomik','harshly','i','will','tear','her','pussy']
for i in list:
    speaker.speak(i)'''
'''lt=time.localtime()
print('The local time is : ',lt)'''
#print(time.strftime('%d|%m|%Y'))
'''speaker=win32com.client.Dispatch('SAPI.SpVoice')
speaker.speak('I')'''
