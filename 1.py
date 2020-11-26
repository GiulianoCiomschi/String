s=str(input("Dati sirul:"))

s_M=0
s_c=0
s_car=0
for i in range(0,(len(s))):
    if (ord(s[i]))<=90 and ((ord(s[i]))>=65):
        s_M+=1
    if (ord(s[i]))<=57 and (ord(s[i]))>=48:
        s_c+=1
    if((ord(s[i]))>=33)and((ord(s[i]))<=47)or((ord(s[i]))>=58)and((ord(s[i]))<=64)or((ord(s[i]))>=91)and((ord(s[i]))<=96)or((ord(s[i]))>=123)and((ord(s[i]))<=127):
        s_car+=1
print("Numarul majuscule este",s_M,sep=" ")
print("Numarul cifre este",s_c,sep=" ")
print("Numarul carcatere speciale este",s_car,sep=" ")