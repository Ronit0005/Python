'''f=open('myfile.txt','r')
while True:
    line=f.readline()
    print(line)
    if not line:
        print(type(line))
        print("Closing all the tabs.......")
        break'''
'''i=0
f=open('myfile2.txt','r')
while True:
    i=i+1
    line=f.readline()
    if not line:
        print("Clearing all the data stored........")#Lines are of type string
        break
    m1=int(line.split()[0])
    m2=int(line.split()[1])
    m3=int(line.split()[2])
    print(f"The marks of the student {i} in the maths is :{m1}")
    print(f"The marks of the student {i} in the maths is :{m2}")
    print(f"The marks of the student {i} in the maths is :{m3}")
    print("\n")
    '''
f=open('myfile.txt','w')
writen=['ronit\n','rahul\n','Rishi\n']
f.writelines(writen)
f.close()