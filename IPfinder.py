#Problem from Elements of Programming Interview in Python, my solution
#Given a string of numbers, find all possible IP addresses, where an IP address is valid if it contains numbers 0 through 9, and 3 periods

def ipaddress_finder(s):
    results = []
    parts = 4*[None]

    def is_valid(octet):
        #print(octet)
        if int(octet) < 255:
            return True
    
    for i in range(1,min(len(s),4)):
        parts[0] = s[:i]
        if is_valid(parts[0]):
            for j in range(1,min(4,len(s) - i)):
                parts[1] = s[i:i+j]
                if is_valid(parts[1]):
                    for k in range(1,min(4,len(s) - i - j)):
                        parts[2] = s[i+j:i+j+k]
                        parts[3] = s[i+j+k:]
                        if is_valid(parts[2]) and is_valid(parts[3]):
                            results.append('.'.join(parts))
    return results
    

print(ipaddress_finder('19216811'))