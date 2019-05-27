#input from user: his ID: if 9 ok, if 8 - add 0 to the start
id =[]
len=int(input("enter length of your id:"))
print("enter your ID: ")
for i in range(0,len):
    id.append(int(input("enter digit: ")))
if len == 8:
    id.insert(0,0)
print("your ID:", id)

count = [1,2,1,2,1,2,1,2,1]
print()
print("the first order:")
print(id)
print(count)
print()
for i in range(0,9):
    id[i]= id[i]*count[i]
print("after 1 round: id*count")
print(id)
print()
print("fix the numbers above 9:")
for i in range(0,9):
    if id[i]>9:
        id[i] = int((id[i]%10) + (id[i]/10))
print(id)
print("calculation:")
sum = 0
for i in range(0,9):
    sum = sum+ id[i]
print(sum)
if (sum%10) != 0:
    print("NOT VALID ID!")
else:
    print("VALID ID!")
