import argparse
import requests
def downloadFile(url,name):
    if name =='None':
      name='ronit'   
    print('Started Downloading......')
    response=requests.get(url)
    open(f'{name}.jpg','wb').write(response.content)
    print('Completed Downloading.....')
    return f'{name}.jpg'
parser=argparse.ArgumentParser()
parser.add_argument('url',help='url of the file to download')
parser.add_argument('-o','--output',help='By which name do you want to save the file',default=None)
args=parser.parse_args()
t=downloadFile(args.url,args.output)
print(t)