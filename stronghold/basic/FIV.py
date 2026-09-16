def resolver_conejos(n, k):
    if n == 1 or n == 2:
        return 1
    
    f_prev2 = 1  # F(n-2)
    f_prev1 = 1  # F(n-1)
    
    for _ in range(3, n + 1):
        f_actual = f_prev1 + k * f_prev2
        f_prev2 = f_prev1
        f_prev1 = f_actual
        
    return f_actual

entrada = input("Introduce los valores de n y k separados por un espacio: ")

n, k = map(int, entrada.split())

resultado = resolver_conejos(n, k)
print(f"Resultado: {resultado}")