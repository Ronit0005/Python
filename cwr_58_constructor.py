class people:
    def __init__(self,name,occupation,netWorth):
        self.name=name
        self.occupation=occupation
        self.netWorth=netWorth
    def profile(self):
        print(f'Name : {self.name}\nOccupation : {self.occupation}\nNet Worth : {self.netWorth}')
ronit=people('Ronit','Businessman','10Crores')
ronit.profile()
rahul=people('Rahul','Software Engineer','2Lakhs')
rahul.profile()
                