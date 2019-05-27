from computer import Computer
from phone import Phone

class Shop:
    supply=[None,None,None,None,None,None]
    # Methods:
    def suggest_sell(self,x):
        if x == 1:
            for i in self.supply:
                if self.supply[i] is Computer:
                    print("Index: {}"),            
        elif x==2:
            for i in self.supply:
                if self.supply[i] is Phone:
                    print("Index: {}"),            
    
    def buy_item(self,index):
        return "price: {}, warranty_years: {}".format(self.supply[index].price, self.supply[index].warranty_years)
        


