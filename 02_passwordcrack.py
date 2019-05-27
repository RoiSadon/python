import passlib.hash

root = "root:$6$Tnd5Ce9O$nNhq84wKYQQwxKGqsBAsIMHIETB9MjOeO9ykuOmW9q6PO1v4qWEuCbfQKYQXK4D2uJjvgrkfnZfcMWqlQhOOm/:17846:0:99999:7:::"
password = '$6$Tnd5Ce9O$nNhq84wKYQQwxKGqsBAsIMHIETB9MjOeO9ykuOmW9q6PO1v4qWEuCbfQKYQXK4D2uJjvgrkfnZfcMWqlQhOOm/'
salt = b'Tnd5Ce9O'
encode = ""
posible_chars = []
password_guess = ""
for i in range(97,123):
    posible_chars.append(chr(i))
for i in range(48,58):
    posible_chars.append(chr(i))


def get_pass(*num):
    password_guess = ""  
    for i in range(6):
        password_guess += posible_chars[num[i]]
    print(str.encode(password_guess))
    return(str.encode(password_guess))


# encode = hashlib.sha512(salt + get_pass(0,1,2,3,4,5)).hexdigest()
# print(encode)
def getpass():
    for i in range(0,36):
        for j in range(0,36):
            for k in range(0,36):
                for l in range(0,36):
                    for m in range(0,36):
                        for n in range(0,36):
                            encode = passlib.hash.sha512_crypt.hash(get_pass(i,j,k,l,m,n), salt="Tnd5Ce9O" ,rounds=5000)
                            #print(len(encode), len(password.encode()), type(encode),type(password))
                            if encode == password:
                                return get_pass(i,j,k,l,m,n)

#encode = hashlib.sha512(salt+get_pass(0,0,0,0,0,0)).hexdigest()
# print(base64.b64decode(encode))
#print(len(encode))
print(getpass())

# # while password != encode:
#     pass_to_decode = b'123456'
#     
