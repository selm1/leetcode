def romanToInt(s: str) -> int:
    out = 0
    hashmap = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    i = len(s) - 1
    while (i > -1):
        print("i: ", i)
        out += hashmap[s[i]]
        if i == 0:
            break
        if s[i] == "X" or s[i] == "V":
            if s[i-1] == "I":
                out -= hashmap[s[i-1]]
                i -= 1
        elif s[i] == "C" or s[i] == "L":
            if s[i-1] == "X":
                out -= hashmap[s[i-1]]
                i -= 1
        elif s[i] == "M" or s[i] == "D":
            if s[i-1] == "C":
                out -= hashmap[s[i-1]]
                i -= 1
        i -= 1
        print("out: ", out)
    return out


print(romanToInt("MMMCDXC"))
