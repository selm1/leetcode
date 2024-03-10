def lengthOfLongestSubstring(s: str) -> int:
    max_length = 0
    current_length = 0
    j = 0
    i = 0
    seen = []
    while j < len(s):
        if s[j] not in seen:
            seen.append(s[j])
            j += 1
        else:
            current_length = len(seen)
            if current_length > max_length:
                max_length = current_length
            i = i + 1
            j = i
            seen = []


    current_length = len(seen)
    if current_length > max_length:
      max_length = current_length
    
    return max_length

print(lengthOfLongestSubstring("dvdf"))
