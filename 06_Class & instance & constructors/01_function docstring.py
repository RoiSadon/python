'''global __doc__'''
def print_max(x,y):
    ''' Function to print max number:'''
    '''won't be printed'''
    x=int(x)
    y=int(y)
    if(x>y):
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')
print_max(3,5)
'''won't be printed'''
# __doc__ - Function to show the note in '''''' (only the first one!) 
# Inside the function: 
print(print_max.__doc__)
# In global area:
print(__doc__)
