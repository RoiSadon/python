b"h

# Exceptions in python:

```python
try:
    num = int(input("enter number: "))
except ValueError:
    print("value error!")
except KeyboardInterrupt:
    print("keyboard interrupt: ")
except OverflowError:
    print("OverflowError: ")
else:
    print("you entered : ", num)
finally:
    print("End")
```

* try - the risky code that can throw an error!
* except + name of error - cases of error, and command to do. 
* else - case the try is worked properly. 
* finally - will run always in any case. 

#### Exception hirarchy buit-in in python:
``` python
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```

### exception in functions: 
```python
def func():
    try:
        num =int(input("enter number:  "))
    except ValueError:
        return "Value error!"
    except KeyboardInterrupt:
        return "keyborad interrupt"
    else:
        return "valid number: {}".format(num)
    finally: 
        print("end!")

a = func()
print("result of function: ", a)

'''
result:
-------------------
enter number:  32
end!
result of function:  valid number 32
'''
```
* note: the finally will be executed first, and always. 

###
### Exception() - built in function in py. 
``` python
try: 
    id = input("Enter your ID:")
    if len(id) < 9:
        raise Exception()
    print("Valid ID")
except Exception:
    print("NOT VALID ID!")
```

### Create class that will inherit from 'Exception' class. 
```python
class A(Exception):
    def __init__(self):
        Exception.__init__(self)

try: 
    id = input("Enter your ID: ")
    if len(id) < 9:
        raise A()
except A:
    print("NOT VALID ID!")
else:
    print("VALID ID!")
finally:
    print("END!")
    
```
* class A inherits from class Exception. 

### Client exception with parameters: 
```python
class A(Exception):
    def __init__(self,length,at_least):
        Exception.__init__(self)
        self.length = length
        self.at_least = at_least

try:
    name = input("Enter your full name: ")
    if len(name) < 5:
        raise A(len(name), 5)
except A:
    print("Your name is too short!")
else:
    print("Your full name is: {}".format(name))
finally:
    print("END!")
```
* note: I called it A for simlicity. (better to write - ShortInputException)

### using 'as'
```python
class A(Exception):
    def __init__(self,length,at_least):
        Exception.__init__(self)
        self.length = length
        self.at_least = at_least

try:
    name = input("Enter your full name: ")
    if len(name) < 5:
        raise A(len(name), 5)
except A as ex:
    print(ex.length, ex.at_least)
else:
    print("Your full name is: {}".format(name))
finally:
    print("END!")
```

### Multi level exception: 

```python
class UnderAgeException(Exception):
    def __init__(self):
        Exception.__init__(self)

class OverAgeException(Exception):
    def __init__(self):
        Exception.__init__(self)

try:
    age = (int)(input("Enter your age: "))
    if age < 0:
        raise UnderAgeException()
    if age > 120:
        raise OverAgeException()
# catches all the exceptions that are from "Exception" class or sub-class
except Exception: 
    print("NOT VALID AGE!")
else:
    print("VALID!")
```
* note: the 'except Exception' will catch all the Exceptions in the class or in the sub-class. 

### We can use specific classes for diffrent error, and also use Exception for all the other errors that inherit from Exception.

```python
class UnderAgeExeption(Exception):
    def __init__(self):
        Exception.__init__(self)

class OverAgeExeption(Exception):
    def __init__(self):
        Exception.__init__(self)

try:
    age = int(input('Enter age: '))
    if age < 0:
        raise UnderAgeExeption()
    if age > 120:
        raise OverAgeExeption()
except OverAgeExeption:
    print("OverAgeExeption non valid age")      
except UnderAgeExeption:
    print("UnderAgeExeption non valid age")    
except Exception:  
    print("non valid age")
else:
    print('valid age')
finally:
    print("End of app")

```


