import textwrap

def wrap(string, max_width):
    strLen = len(string)
    if(strLen > 0 and strLen < 1000 and max_width > 0 and max_width < strLen):
        return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)