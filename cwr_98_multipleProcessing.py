'''import multiprocessing
import requests
def downloadFiles(url,name):
    print('Started downloading files')
    response=requests.get(url)
    open (f'{name}.jpg','wb').write(response.content)
    print("Finishing the download")
if __name__=='__main__':
 url='https://picsum.photos/2000/3000'
 for i in range(5):
    downloadFiles(url,i)
 pros=[]
 for i in range(5):
    p=multiprocessing.Process(target=downloadFiles,args=[url,i])
    p.start()
    pros.append(p)
 for p in pros:
    p.join()'''
from concurrent.futures import ProcessPoolExecutor
import requests
def downloadFiles(url,name):
    print("Started Download")
    response=requests.get(url)
    open (f'photo{name}.jpg','wb').write(response.content)
    print('Finished Download')
if __name__=='__main__':
 url='https://picsum.photos/2000/3000'
 def processTest():
    with ProcessPoolExecutor() as executor:
      l1=[url for i in range(5)]
      l2=[i for i in range(5)]
      results=executor.map(downloadFiles,l1,l2)
      for result in results:
        print(result)
 processTest()
 