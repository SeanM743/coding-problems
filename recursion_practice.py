#Let's rework the phone pad combination problem

def keypad(pnum):

    mappings = {'0':'0','1':'1','2':'ABC','3':'DEF','4':'GHI','5':'JKL','6':'MNO','7':'PRS',
    '8':'TUV','9':'WXY'}

    def combinations(digits,leftover):

        if leftover == '':
            result.append(digits)
        else:
            for digit in mappings[leftover[0]]:
                combinations(digits + digit,leftover[1:])

    result = []
    combinations('',pnum)
    return result

a = keypad('8675309')

#Let's try a variation of the above

def keypad_variation(pnum):
    mappings = {'0':'0','1':'1','2':'ABC','3':'DEF','4':'GHI','5':'JKL','6':'MNO','7':'PRS',
    '8':'TUV','9':'WXY'}

    def combinations(prefs, leftover):
        
        ltrs = []
        for pre in prefs:
            for ltr in mappings[leftover[0]]:
                ltrs.append(pre + ltr)
        return ltrs

    result = ['']
    for dig in pnum:
        result = combinations(result,dig)
    return result

b = keypad_variation('8675309')

print(a==b)
#Let's do the basic permutation problem

def perm(s):

    if len(s) == 1:
        return s[0]
    t = []
    for ltr in s:
        leftover = [l for l in s if l != ltr]

        for z in perm(leftover):
            t.append(ltr + ''.join(z))

    return t

print(perm('ABC'))