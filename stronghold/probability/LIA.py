from math import comb


def independent_alleles_prob(k: int, N: int) -> float:
    total_organisms = 2**k
    p = 0.25

    prob_at_least_N = sum(
        comb(total_organisms, i) * (p**i) * ((1 - p) ** (total_organisms - i))
        for i in range(N, total_organisms + 1)
    )

    return prob_at_least_N


k = int(input("Enter k (number of generations): "))
N = int(input("Enter N (minimum number of Aa Bb offspring): "))

result = independent_alleles_prob(k, N)
print(f"Probability: {result:.3f}")