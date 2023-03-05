def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False

    if x <= 9:
        return True

    else:
        x = str(x)
        for i in range(len(x) // 2):
            if x[i] != x[-i - 1]:
                return False

        return True


print(isPalindrome(98))
