def longestPalindrome(s):
    if len(s) == 1:
        return 1

    length = 0
    d = {c: s.count(c) for c in s}

    odd_len = 0
    for key, value in d.items():
        if value % 2 != 1:
            length += value
        elif value % 2 == 1:
            length += value - 1
            if value > odd_len:
                odd_len = value

    return length + (1 if odd_len > 0 else 0)


print(longestPalindrome("abccccdd"))
