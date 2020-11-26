s=str(input("Dati IDNP:"))
n=True
if len(s)==13:
    for i in s:
        if (ord(i))>=48 and (ord(i))<=57:
            n=True
        else:
            n=False
elif len(s)!=13:
    print("IDNP dvs. este gresit")
if n==True:
    print("IDNP dvs. este corect")
else:
    print("IDNP dvs. este incorect")
