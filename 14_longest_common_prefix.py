def longestCommonPrefix(strs):
    prefix = min(strs, key=len)
    i = 0
    j = len(prefix)
    while True:
        longest = True
        for s in strs:
            if not s.startswith(prefix):
                longest = False
        if longest:
            break
        j -= 1
        prefix = prefix[i:j]
        if prefix == "":
            break

    return prefix


print(longestCommonPrefix(["reflower", "flow", "flight"]))
