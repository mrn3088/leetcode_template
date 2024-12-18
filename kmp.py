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
    i, j = 0, 0
    while i < len(s):
        if s[i] == pattern[j]:
            i += 1
            j += 1
        elif j > 0:
            j = nxt[j - 1]
        else:
            i += 1
        if j == len(pattern):
            return i - j
    return -1
