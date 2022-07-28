def isAnyAlphaNumeric(s):
    result = False
    for i in s:
        if (i.isalnum()):
            result = True
    return result

def isAnyDigit(s):
    result = False
    for i in s:
        if (i.isdigit()):
            result = True
    return result

def isAnyAlpha(s):
    result = False
    for i in s:
        if (i.isalpha()):
            result = True
    return result

def isAnyLower(s):
    result = False
    for i in s:
        if (i.islower()):
            result = True
    return result

def isAnyUpper(s):
    result = False
    for i in s:
        if (i.isupper()):
            result = True
    return result

if __name__ == '__main__':
    s = input()
    if (len(s) < 1 or len(s) > 1000): exit();
    
    
    print(isAnyAlphaNumeric(s))
    print(isAnyAlpha(s))
    print(isAnyDigit(s))
    print(isAnyLower(s))
    print(isAnyUpper(s))