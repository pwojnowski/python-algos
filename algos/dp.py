def number_factor_dp(x: int, factors: list):
    """Calculate the number of distinct factors of number X, obtained from given numbers."""
    if x <= 3:
        return 1
