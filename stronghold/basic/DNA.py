def main():
    count()
def count():
    code = input("Ingrese la cadena de ADN: ")
    Adenina = 0
    Timina = 0
    Citosina = 0
    Guanina = 0
    for i in range(len(code)):
        letra = code[i]
        if letra == "A":
            Adenina += 1
        elif letra == "T":
            Timina += 1
        elif letra == "C":
            Citosina += 1
        elif letra == "G":
            Guanina += 1
    print(Adenina, Citosina, Guanina, Timina)

main()