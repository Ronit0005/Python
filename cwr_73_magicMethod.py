class employee:
    name='Ronit'
    def __init__(self):
        print("I am a constructor !")
    def __len__(self):
        l=0
        for i in self.name:
            l+=1
        return l
    def __call__(self):
        print('I am a call method')
    def __str__(self):
        return f'I am a str method'
    def __repr__(self):
        return 'I am a repr method'
obj=employee()
#print(len(obj))
#obj()
#print(obj)
#print(str(obj))
#print(repr(obj))