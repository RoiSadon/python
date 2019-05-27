# Python modules for security:

### OS - Operating System: 
```python
import os

# 'dir' function will show us all the functions the module has
print(dir(os))

# get current working directory: gets the path of the file. 
print(os.getcwd())

# change directory for this file
os.chdir('C:/Users/raya/Desktop')
print(os.getcwd())

# list directory: will list files in the currend directory, 
# or in specific path. 
files = os.listdir("/Users/raya/Desktop")
for f in files:
    print(f)

# make directory in given path: 
os.mkdir('C:/Users/raya/Desktop/x')
print(os.listdir('C:/Users/raya/Desktop'))

# make 2 directories at once: 
os.makedirs('C:/Users/raya/Desktop/github/py/newFolder/subFolder')

# remove one dircetory:
os.rmdir('C:/Users/raya/Desktop/github/py/newFolder/subFolder')

# rename file/folder. first the existing file, the changed name. 
os.rename('try.py','demo.py')

# will show info about the file: 
print(os.stat('main.py'))
# st_size is the file size in bytes. 
print(os.stat('main.py').st_size)
# last modification time (return timestamp): 
# to make it readable - we use datetime.fromtimestamp module
from datetime import datetime
mod_time = os.stat('main.py').st_mtime
print(datetime.fromtimestamp(mod_time))

# tree of files: very useful thing:
for dirpath, dirname, filename in os.walk('C:/Users/raya/Desktop/'):
    print('Current path: ', dirpath)
    print('Directories: ', dirname)
    print('Files: ', filename)
    print()
```
