def isPalindrome(s):
    s = s.lower().strip()
    s = ''.join([c for c in s if c.isalnum()])
    reverse = ''.join([s[i] for i in range(len(s) - 1, -1, -1)])
    if reverse == s:
        return True
    return False
