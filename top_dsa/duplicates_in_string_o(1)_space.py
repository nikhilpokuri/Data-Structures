def duplicates(s):
    s = list(s)
    s.sort()

    i = 1
    while i < len(s):
        count = 1
        while i < len(s) and s[i-1] == s[i]:
            count += 1
            i += 1
        if count > 1:
            print(f'{s[i-1]}:{count}')
        i += 1
duplicates('niickk')