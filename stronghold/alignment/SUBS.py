def encontrar_motivo():
    print("Introduce la cadena principal (s):")
    s = input().strip()
    
    print("Introduce la subcadena a buscar (t):")
    t = input().strip()
    
    posiciones = []
    len_s = len(s)
    len_t = len(t)
    
    for i in range(len_s - len_t + 1):
        if s[i : i + len_t] == t:
            posiciones.append(i + 1)
            
    resultado = " ".join(map(str, posiciones))
    print("\nResultado:")
    print(resultado)

if __name__ == "__main__":
    encontrar_motivo()