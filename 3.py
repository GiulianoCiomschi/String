s1=str(input("Dati sirul:"))
s2=str(input("Dati sirul:"))
s3=str(input("Dati sirul:"))
s4=str(input("Dati sirul:"))
s=" "
if (len(s1) and len(s2) and len(s3) and len(s4))>2:
    s= s1[0:2]+s2[0:1]+s3[0:3]+s4[0:len(s4)//2]
    print(s)
elif (len(s1) and len(s2) and len(s3) and len(s4))<2:
    print("Alegeti alte siruri")