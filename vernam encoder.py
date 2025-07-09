import random

key=[]
cipher=[]

def xor(a,b):
    if a == b:
        return "0"
    else:
        return "1"

def encrypt(c):
    global key
    global cipher
    k=random.randint(33,126)
    key.append(chr(k))
    casc=ord(c)
    cbin=format(casc,"08b")
    kbin=format(k,"08b")
    cibin=[]
    for i in range(8):
        cibin.append(xor(cbin[i],kbin[i]))
    cipher.append(str(int("".join(cibin),2)))

plain=input("plaintext:\n")
for c in plain:
    encrypt(c)

print("\nciphertext:\n" + " ".join(cipher))
print("\nkey:\n" + "".join(key))
