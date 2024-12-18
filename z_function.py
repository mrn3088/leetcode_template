def calculate_z(s: str) -> list[int]:
    """
    Calculate the z value array. (Longest Common Prefix)
    z[i] is the longest length where s[:z[i]] == s[i:i+z[i]]
    """
    n = len(s)
    Z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            Z[i] = min(Z[i - l], r - i + 1)
        while Z[i] + i < n and s[Z[i]] == s[Z[i] + i]:
            Z[i] += 1
        if Z[i] + i - 1 > r:
            l, r = i, Z[i] + i - 1
    return Z
