def longestCommonPrefix(strs: list):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 1:
        return strs[0]

    prefix = ""
    smallest_word = min(strs, key=len)
    print(smallest_word)

    for i in range(len(smallest_word)):
        for word in strs:
            if i == len(word) or word[i] != smallest_word[i]:
                return prefix
        prefix += smallest_word[i]

    return prefix


print(longestCommonPrefix(["flower","flow","flight"]))
