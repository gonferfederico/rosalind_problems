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

def longest_common_substring(sequences):
    if not sequences:
        return ""
    
    sequences.sort(key=len)
    shortest_seq = sequences[0]
    n = len(shortest_seq)
    
    for length in range(n, 0, -1):
        for start in range(n - length + 1):
            substr = shortest_seq[start:start + length]
            if all(substr in seq for seq in sequences[1:]):
                return substr
                
    return ""

print("Pega tus secuencias en formato FASTA y presiona Enter en una línea vacía para calcular:")
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
dna_sequences = parse_fasta(fasta_input)
result = longest_common_substring(dna_sequences)

print("\nResultado:")
print(result)