#Reading a file 
'''f=open('minefile.txt')
#print(f)
text=f.read()
print(text)
f.close()
#fo=open('myfile.txt','w')#a new file is created .
f=open('minefile.txt','a')'''
#writing a file 
'''f=open('minefile.txt','w')
f.write("Hello world This is a new world !!!")
f.close()'''
#Appending a file 
'''f=open('minefile.txt','a')
f.write("Hello world This Is again a new  world !!!!!!!!")
f.close()'''
#with keyword
with open('minefile.txt','a') as f:
    f.write("I am in with :")