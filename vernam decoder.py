plain=[]
def xor(a,b):
    if a == b:
        return "0"
    else:
        return "1"

def decode(k,ci):
    global plain
    kbin=format(ord(k),"08b")
    cibin=format(ci,"08b")
    pbin=[]
    for j in range(8):
        pbin.append(xor(kbin[j],cibin[j]))
    plain.append(chr(int("".join(pbin),2)))

print("ciphertext:")
cipher=list(map(int,input().split()))
print("\nkey:")
key=input()

for i in range(len(cipher)):
    decode(key[i],cipher[i])

print("\nplaintext:\n" + "".join(plain))