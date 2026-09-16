import sys

def traducir_rna(rna: str) -> str:
    tabla_codones = {
        'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
        'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
        'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
        'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
        'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
        'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
        'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
        'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
        'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
        'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
        'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
        'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
        'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
        'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
        'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
        'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
    }
    
    proteina = []
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if len(codon) == 3:
            aminoacido = tabla_codones.get(codon)
            if aminoacido == 'Stop' or aminoacido is None:
                break
            proteina.append(aminoacido)
            
    return "".join(proteina)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Por favor, indica el archivo de texto.")
        print("Uso: python traductor.py nombre_archivo.txt")
        sys.exit(1)
        
    archivo_origen = sys.argv[1]
    
    try:
        with open(archivo_origen, 'r') as f:
            secuencia_rna = f.read().strip().replace('\n', '').replace('\r', '')
            
        resultado = traducir_rna(secuencia_rna)
        print(resultado)
        
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{archivo_origen}'.")
        sys.exit(1)