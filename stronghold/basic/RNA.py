
def convert():
    RNAm = []
    cadena = input("Ingrese la cadena de ADN: ")
    for i in cadena:
        if i == "T":
            RNAm.append("U")
        else:
            RNAm.append(i)

    print("".join(RNAm))
convert()
