def number_factor_dp(x: int, factors: list):
    """Find the number of ways to express x as the sum of given factors."""
    # idx 0 = 1, because it's the number of times a factor equal i can fit in i.
    # Another words: a number can contains itself once.
    count = [1, 1, 1, 2]
    if x == 0:
        return 0
    if x <= 3:
        return count[x]
    for i in range(4, x + 1):
        total = 0
        for f in factors:
            if i >= f:
                total += count[i-f]
        count.append(total)
    return count[x]
