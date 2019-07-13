'''Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given 
below. Note that 1 does not map to any letters.'''

'''Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].'''



def phone_comb(pnum):
    MAPPINGS = ['0','1','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

    def combine(digits,leftover):
        if leftover == '':
            result.append(digits)

        else:
            for ltr in MAPPINGS[ord(leftover[0]) - ord('0')]:
                combine(digits + ltr, leftover[1:])               
        return result
    
    result = []
    combine('', pnum)

    return result

#print(phone_comb('8439615'))

def combinations(pnum):
    d = {'0': '0','1':'1','2':'ABC','3':'DEF','4':'HIJ','5':'JKL',
    '6':'MNO','7':'PQRS','8':'TUV','9':'WXYZ'}

    def combine_helper(pres,leftover):

        partial = []
        for pre in pres:
            for ltr in d[leftover[0]]:
                partial.append(pre+ltr)
        
        return partial

    result = ['']

    for digit in pnum:
        result = combine_helper(result,digit)
    
    return result
print(combinations('8439171'))