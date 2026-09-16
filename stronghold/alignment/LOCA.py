import io
from Bio import SeqIO
from Bio.Align import substitution_matrices

def resolver_alineamiento_local():
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
    
    pam250 = substitution_matrices.load("PAM250")
    gap_penalty = -5
    
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    max_score = 0
    max_i, max_j = 0, 0
    
    for i in range(1, m + 1):
        char_s = s[i-1]
        for j in range(1, n + 1):
            char_t = t[j-1]
            
            score_match = pam250.get((char_s, char_t), pam250.get((char_t, char_s), -4))
            
            match_mismatch = dp[i-1][j-1] + score_match
            gap_in_t = dp[i-1][j] + gap_penalty
            gap_in_s = dp[i][j-1] + gap_penalty
            
            dp[i][j] = max(0, match_mismatch, gap_in_t, gap_in_s)
            
            if dp[i][j] > max_score:
                max_score = dp[i][j]
                max_i, max_j = i, j
                
    curr_i, curr_j = max_i, max_j
    res_s = []
    res_t = []
    
    while curr_i > 0 and curr_j > 0 and dp[curr_i][curr_j] > 0:
        char_s = s[curr_i-1]
        char_t = t[curr_j-1]
        score_match = pam250.get((char_s, char_t), pam250.get((char_t, char_s), -4))
        
        if dp[curr_i][curr_j] == dp[curr_i-1][curr_j-1] + score_match:
            res_s.append(char_s)
            res_t.append(char_t)
            curr_i -= 1
            curr_j -= 1
        elif dp[curr_i][curr_j] == dp[curr_i-1][curr_j] + gap_penalty:
            res_s.append(char_s)
            curr_i -= 1
        elif dp[curr_i][curr_j] == dp[curr_i][curr_j-1] + gap_penalty:
            res_t.append(char_t)
            curr_j -= 1
            
    substring_r = "".join(reversed(res_s)).replace("-", "")
    substring_u = "".join(reversed(res_t)).replace("-", "")
    
    print("\nResultado:")
    print(int(max_score))
    print(substring_r)
    print(substring_u)

if __name__ == "__main__":
    resolver_alineamiento_local()