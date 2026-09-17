def dominant_allele_prob(k: int, m: int, n: int) -> float:
    t = k + m + n
    total_pairs = t * (t - 1) / 2

    recessive_outcomes = (
        (n * (n - 1) / 2) * 1.0  # aa x aa
        + (m * n) * 0.5  # Aa x aa
        + (m * (m - 1) / 2) * 0.25  # Aa x Aa
    )

    return 1.0 - (recessive_outcomes / total_pairs)


# Prompt for each value individually
k = int(input("Enter k (homozygous dominant): "))
m = int(input("Enter m (heterozygous): "))
n = int(input("Enter n (homozygous recessive): "))

result = dominant_allele_prob(k, m, n)
print(f"Probability: {result:.5f}")