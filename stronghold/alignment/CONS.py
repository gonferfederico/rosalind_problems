import sys

def parsear_fasta(lineas_input):
 
    secuencias = []
    secuencia_actual = []
    
    for linea in lineas_input:
        linea = linea.strip()
        if not linea:
            continue
        if linea.startswith(">"):
            if secuencia_actual:
                secuencias.append("".join(secuencia_actual))
                secuencia_actual = []
        else:
            secuencia_actual.append(linea)
            
    if secuencia_actual:
        secuencias.append("".join(secuencia_actual))
        
    return secuencias

def resolver_consenso_y_perfil():
    print("Introduce el dataset en formato FASTA (presiona Ctrl+D en Linux/Mac o Ctrl+Z en Windows al terminar para procesar):")
    

    input_usuario = sys.stdin.read().splitlines()
    
    secuencias = parsear_fasta(input_usuario)
    if not secuencias:
        print("No se encontraron secuencias válidas.")
        return

    longitud = len(secuencias[0])
    
    perfil = {
        'A': [0] * longitud,
        'C': [0] * longitud,
        'G': [0] * longitud,
        'T': [0] * longitud
    }
    
    for seq in secuencias:
        for i, nucleotido in enumerate(seq):
            if nucleotido in perfil:
                perfil[nucleotido][i] += 1

    consenso = []
    bases = ['A', 'C', 'G', 'T']
    for i in range(longitud):
        base_maxima = max(bases, key=lambda base: perfil[base][i])
        consenso.append(base_maxima)
        
    cadena_consenso = "".join(consenso)
    
    print("\n--- Resultado ---")
    print(cadena_consenso)
    for base in bases:
        valores_formateados = " ".join(map(str, perfil[base]))
        print(f"{base}: {valores_formateados}")

if __name__ == "__main__":
    resolver_consenso_y_perfil()