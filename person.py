
class person():
    
    def __init__(self,name):
        
        self.name = name
        self.total_owed = 0
        self.transaction_list = []

class user(person):
    
    def __init__(self):
        
        person.__init__(self, "User")
        
        
        