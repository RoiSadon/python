from computer import Computer
from phone import Phone
from shop import Shop
from electronicItems import ElectronicItems

my_shop = Shop()

my_shop.supply[0]=Computer(True,3000,1000,4,100)
my_shop.supply[1]=Computer(True,5000,1500,5,150)
my_shop.supply[2]=Computer(False,1500,1200,1,0)

my_shop.supply[3]=Phone(True,"0504323445",1000,200,7,50,)
my_shop.supply[4]=Phone(True,"5436754332",6000,500,2,20)
my_shop.supply[5]=Phone(True,"2345786575",1500,300,1,100)


# First sell:
print('-'*100)
# get all Computers info in the shop:
print("------All Computers in supply:------")
for i in range(0,len(my_shop.supply)):
    if type(my_shop.supply[i]) is Computer:
        print(my_shop.supply[1].print_info())
print('-'*100)

# Buy computer as my wish:
print("------You bought computer:------")
print(my_shop.buy_item(1))
print('-'*100)
print("Charge: ")
print(my_shop.supply[1].end_of_charge())


print('-'*100)
# get all Phones info in the shop:
print("------All Phones in supply:------")
for i in range(0,len(my_shop.supply)):
    if type(my_shop.supply[i]) is Phone:
        print(my_shop.supply[1].print_info())
print('-'*100)

# Buy phone as my wish:
print("------You bought phone:------")
print(my_shop.buy_item(4))
print('-'*100)
print("Charge: ")
print(my_shop.supply[4].end_of_charge())