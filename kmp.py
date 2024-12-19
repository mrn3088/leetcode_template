def build_next(pattern: str) -> list[int]:
    """
    Calculating next array
    """
    nxt = [0] * len(pattern)
    j = 0  # prefix_len
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = nxt[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        nxt[i] = j
    return nxt


def kmp(s: str, pattern: str) -> int:
    """
    Find the first index of pattern in string s
    """
    nxt = build_next(pattern)
    n, m = len(s), len(pattern)
    j = 0
    for i in range(n):
        while j > 0 and s[i] != pattern[j]:
            j = nxt[j - 1]
        if s[i] == pattern[j]:
            j += 1
        if j == m:
            return i - j + 1
    return -1
