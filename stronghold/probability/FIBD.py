def mortal_fibonacci_rabbits(n: int, m: int) -> int:
    # ages[i] represents rabbit pairs of age i months
    # A rabbit pair lives for m months (ages 0 to m - 1)
    ages = [0] * m
    ages[0] = 1  # Month 1: 1 newborn pair

    for _ in range(1, n):
        # All rabbits aged 1 to m-1 can reproduce (1 pair of offspring each)
        newborns = sum(ages[1:])

        # Shift ages: rabbits get 1 month older; those of age m-1 die
        ages = [newborns] + ages[:-1]

    return sum(ages)


# Prompt for each value individually
n = int(input("Enter n (number of months): "))
m = int(input("Enter m (lifespan in months): "))

result = mortal_fibonacci_rabbits(n, m)
print(f"Total rabbit pairs: {result}")