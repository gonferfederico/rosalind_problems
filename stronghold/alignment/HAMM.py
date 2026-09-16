def calcular_hamming():
    s = input().strip()
    t = input().strip()
    
    distancia = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            distancia += 1
            
    print(distancia)

calcular_hamming()