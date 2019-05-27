# HOMEWORK1 raya hazi
num = int(input("Enter number please:"))

if num>0 and num <10:
    print("number with 1 digit:", str(num))
elif num>9 and num<100:
    print("number with 2 digits:", num)
    sum = num/10 + num%10
    print ("2 digits:" , int(sum))
elif num > 99 and num<1000:
    print("number with 3 digits:", num)
    sum = int(num/10/10)* int(num/10%10) * int(num%10)
    print("3 digits:", int(sum))
else:
    print("the number is bigger than 3 digits")
