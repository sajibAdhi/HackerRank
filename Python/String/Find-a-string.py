def count_substring(string, sub_string):
    if(len(string) < 1 or len(string) > 200): return
    
    loop = 0
    count = 0
    while loop < len(string)-len(sub_string)+1:
        response = string[loop: loop + len(sub_string)].find(sub_string)
        if(  response == 0): 
            count = count +1
        loop = loop+1
        
    return count

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count