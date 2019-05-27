
# in this program - 
#we see what inside the function doesn't change the outside value-x
# Outside x=50. in func- x-2;

x=50
def func(x):
    print('x is',x)
    x=2
    print('changed local to x',x)
func(x)
print('x is still',x)


