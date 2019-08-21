# the code is limited till 3 employes and 3 months, simply go and increase variables if you want to plot more data. 


import matplotlib.pyplot as plt 

class month_sell : 
    
    def __init__(self, sellA , sellB , sellC) : 
        
        self.sellA = sellA
        self.sellB = sellB
        self.sellC = sellC
        

    def month_graph (self) : 
        
        month = ["month1", "month2", "month3"]
        
        user2 = [self.sellA, self.sellB, self.sellC]
        
        plt.plot(month, user2)
        plt.show()
        
    def add (self) : 
            
            return (self.sellA+self.sellB+self.sellC)

print ("enter the sells of employe1:")

sell1 = int (input("enter the sell of first month :")) 
sell2 = int (input("enter the sell of second month :"))
sell3 = int(input("enter the sell of third month : "))

print ("enter the sells of employe2 :")

sell4 = int (input("enter the sell of first month : "))
sell5 = int(input("enter the sell of second month : "))
sell6 = int(input("enter the sell of third month : "))

print ("enter the sell of employe3:")

sell7 = int (input("enter the sell of first month:"))
sell8 = int (input("enter the sell of second month :"))
sell9 = int (input("enter the sell of third month :"))

employe1 = month_sell(sell1 , sell2 , sell3)
employe1.month_graph()

employe2 = month_sell(sell4 , sell5 , sell6)
employe2.month_graph()

employe3 = month_sell(sell7 , sell8 , sell9)
employe3.month_graph()

command1 = input ("do you want to plot total sell of each employe?")

if command1 == 'yes' : 

    employe1 = month_sell(sell1, sell2 , sell3)
    user1 = employe1.add()
    
    employe2 = month_sell(sell4, sell5 , sell6)
    user2 = employe2.add()
    
    employe3 = month_sell(sell7 , sell8, sell9)
    user3 = employe3.add()

    total_sell = [user1, user2, user3]
    employe = ["employe1", "employe2", "employe3"]
    
    plt.bar(employe, total_sell)
    plt.show()
    




