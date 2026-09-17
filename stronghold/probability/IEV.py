def expected_dominant_offspring(
    aa_aa: int,
    aa_aa_het: int,
    aa_recessive: int,
    het_het: int,
    het_recessive: int,
    recessive_recessive: int,
) -> float:
    return (
        2.0 * aa_aa
        + 2.0 * aa_aa_het
        + 2.0 * aa_recessive
        + 1.5 * het_het
        + 1.0 * het_recessive
        + 0.0 * recessive_recessive
    )


c1 = int(input("Enter number of AA-AA couples: "))
c2 = int(input("Enter number of AA-Aa couples: "))
c3 = int(input("Enter number of AA-aa couples: "))
c4 = int(input("Enter number of Aa-Aa couples: "))
c5 = int(input("Enter number of Aa-aa couples: "))
c6 = int(input("Enter number of aa-aa couples: "))

result = expected_dominant_offspring(c1, c2, c3, c4, c5, c6)
print(f"Expected dominant offspring: {result}")