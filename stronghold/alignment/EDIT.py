import sys

def parse_fasta(fasta_data):
    sequences = []
    current_seq = []
    for line in fasta_data.strip().split('\n'):
        if line.startswith('>'):
            if current_seq:
                sequences.append("".join(current_seq))
                current_seq = []
        else:
            current_seq.append(line.strip())
    if current_seq:
        sequences.append("".join(current_seq))
    return sequences

def edit_distance(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
        
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                cost = 0
            else:
                cost = 1
            
            dp[i][j] = min(
                dp[i - 1][j] + 1,      
                dp[i][j - 1] + 1,      
                dp[i - 1][j - 1] + cost 
            )
            
    return dp[m][n]

print("Pega tus dos secuencias en formato FASTA y presiona Enter en una línea vacía:")
lines = []
while True:
    try:
        line = input()
        if not line:
            break
        lines.append(line)
    except EOFError:
        break

fasta_input = "\n".join(lines)
sequences = parse_fasta(fasta_input)

if len(sequences) >= 2:
    s, t = sequences[0], sequences[1]
    result = edit_distance(s, t)
    print("\nDistancia de edición:")
    print(result)
else:
    print("\nError: Se necesitan al menos dos secuencias en formato FASTA.")