if __name__ == '__main__':
    n = int(input())
    
    n = n+1;
    output = None
    for i in range(1,n):
        if output is None:
            output = str(i)
        else:
            output = output + str(i)
            
    print(output)