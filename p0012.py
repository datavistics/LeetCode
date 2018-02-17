def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    out_list = []
    for _ in range(4):
        out_list.append(num % 10)
        num = num // 10

    print(out_list)


    def rom_digit(d, l):
        rom_list = ['', l[0], l[0]*2, l[0]*3, l[0]+l[1], l[1], l[1]+l[0], l[1]+l[0]*2, l[1]+l[0]*3, l[0]+l[2]]
        return rom_list[d]
    ts = 'M' * out_list[-1]
    hs = rom_digit(out_list[-2], 'CDM')
    tes = rom_digit(out_list[-3], 'XLC')
    os = rom_digit(out_list[0], 'IVX')
    return ts+hs+tes+os

print(intToRoman(1))

print('tsest')