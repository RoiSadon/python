x=50

def func():
    global x
    print('x is:',x)
    x=2
    print('x is:',x)
func()
print('value of x now:',x)

'''
OUTPUT:
________

x is: 50
x is: 2
value of x now: 2
'''