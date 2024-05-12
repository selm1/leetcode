def isValid(s: str) -> bool:
    para = {"}": "{", ")": "(", "]": "["}
    if len(s) == 1 or s[0] in para or len(s) % 2 == 1:
        return False
    stack = []
    for i in range(len(s)):
        if (s[i] == ")" or s[i] == "]" or s[i] == "}") and len(stack) != 0:
            if stack[-1] == para[s[i]]:
                stack.pop()
                continue
            else:
                return False
        stack.append(s[i])

    if len(stack) == 0:
        return True
    return False


print(isValid("(]"))
