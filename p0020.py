def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    stack = []
    d = {'{': '}', '(': ')', '[': ']'}
    symbols = set(('(', '[', '{'))
    for letter in s:
        if letter in symbols:
            stack.append(letter)
        else:
            if not stack or letter != d[stack.pop()]:
                return False
    return stack == []

print(isValid('{{})'))

