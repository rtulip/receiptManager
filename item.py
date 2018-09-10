
class item():
    
    def __init__(self,name,amount,list_of_people):
        
        self.name = name
        self.amount = amount
        self.list_of_people = list_of_people
        self.amount_per_person = self.amount / float(len(self.list_of_people))
        
        