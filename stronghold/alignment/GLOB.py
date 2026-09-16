import io
from Bio import SeqIO
from Bio.Align import substitution_matrices

def resolver_alineamiento_global():
    print("Por favor, pega el bloque de datos en formato FASTA (presiona Enter y luego Ctrl+D o Ctrl+Z según tu sistema para finalizar):")
    
    lineas = []
    try:
        while True:
            linea = input()
            lineas.append(linea)
    except EOFError:
        pass
    
    data_input = "\n".join(lineas)
    
    secuencias = []
    for record in SeqIO.parse(io.StringIO(data_input), "fasta"):
        secuencias.append(str(record.seq))
    
    if len(secuencias) < 2:
        print("Error: Se necesitan al menos dos secuencias en formato FASTA.")
        return
    
    s = secuencias[0]
    t = secuencias[1]
    
    blosum62 = substitution_matrices.load("BLOSUM62")
    
    gap_penalty = -5
    
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        dp[i][0] = dp[i-1][0] + gap_penalty
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j-1] + gap_penalty
        
    for i in range(1, m + 1):
        char_s = s[i-1]
        for j in range(1, n + 1):
            char_t = t[j-1]
            
            score_match = blosum62.get((char_s, char_t), blosum62.get((char_t, char_s), -4))
            
            match_mismatch = dp[i-1][j-1] + score_match
            gap_in_t = dp[i-1][j] + gap_penalty
            gap_in_s = dp[i][j-1] + gap_penalty
            
            dp[i][j] = max(match_mismatch, gap_in_t, gap_in_s)
            
    print("\nResultado:")
    print(int(dp[m][n]))

if __name__ == "__main__":
    resolver_alineamiento_global()