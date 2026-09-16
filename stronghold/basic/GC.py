def calcular_gc(secuencia):
    gc_count = secuencia.count('G') + secuencia.count('C')
    return (gc_count / len(secuencia)) * 100

def resolver_rosalind():
    print("Pega el dataset FASTA y presiona Enter en una linea vacia para procesar:")
    lineas = []
    while True:
        try:
            linea = input()
            if not linea:
                break
            lineas.append(linea)
        except EOFError:
            break
            
    secuencias = {}
    id_actual = ""
    
    for linea in lineas:
        if linea.startswith('>'):
            id_actual = linea[1:]
            secuencias[id_actual] = ""
        else:
            secuencias[id_actual] += linea.strip()
            
    max_id = ""
    max_gc = -1.0
    
    for id_seq, seq in secuencias.items():
        porcentaje_gc = calcular_gc(seq)
        if porcentaje_gc > max_gc:
            max_gc = porcentaje_gc
            max_id = id_seq
            
    print(max_id)
    print(f"{max_gc:.6f}")

resolver_rosalind()