def convert():
    DNAc = []
    cadena = input("Ingrese la cadena de ADN: ")
    for i in cadena:
        if i == "T":
            DNAc.append("A")
        elif i == "A":
            DNAc.append("T")
        elif i == "C":
            DNAc.append("G")
        elif i == "G":
            DNAc.append("C")
        else:
            DNAc.append(i)

    print("".join(DNAc)[::-1])
convert()
