def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if not s:
        return ''
    if numRows == 1:
        return s

    out = [''] * numRows
    cur_ind = 0
    for i, letter in s:
        print(cur_ind)
        out[cur_ind] += letter
        if cur_ind == numRows - 1:
            change = -1
        elif cur_ind == 0:
            change = 1
        cur_ind += change

    return ''.join(out)


t = convert('PAYPALISHIRING', 3)

print(t)
