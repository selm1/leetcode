def longestPalindrome(s):
    length = 0
    l = 0
    r = 0
    # Go through each character
    for k in range(len(s)):

        # Pointors both initially at the same place
        i, j = k, k  # (odd case)

        # While still in bound
        while i >= 0 and j <= (len(s) - 1) and length != len(s):
            if s[i] == s[j]:
                if (j-i+1) > length:
                    length = j - i + 1
                    l = i
                    r = j
                i -= 1
                j += 1
            else:
                break

        i, j = k, k+1  # (even case)
        # While still in bound
        while i >= 0 and j <= (len(s) - 1) and length != len(s):
            if s[i] == s[j]:
                if (j-i+1) > length:
                    length = j - i + 1
                    l = i
                    r = j
                i -= 1
                j += 1
            else:
                break

    return s[l:r+1]


print(longestPalindrome("abb"))
