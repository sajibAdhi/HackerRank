if __name__ == '__main__':
    n = int(raw_input())
    
    if 2 <= n and n <= 10:
        
        def inputCheck(num):
            num = int(num)
            if -100 <= num and num <= 100:
                return num
            
        arr = map(inputCheck, raw_input().split())[0:n]
        elements = list(arr)
        
        if len(elements) == n:
            
            maxElement = max(elements)
            lessThanMax = None
            
            for element in elements:
                if maxElement > element:
                    if (lessThanMax is None):
                        lessThanMax = element
                    elif(lessThanMax < element):
                        lessThanMax = element
            
            print(lessThanMax)