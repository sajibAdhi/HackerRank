
def minion_game(string):
    consonants = 0
    vowels = 0
    
    strLen = len(string)
    if(0 < strLen and strLen < 10**6): 
        for i in range(strLen):
            for j in range(1,strLen+1):
                subStr = string[i:j]
                if( 1 > len(subStr)): continue
                if(
                    subStr[0] == "A" 
                    or subStr[0] == "E" 
                    or subStr[0] == "I" 
                    or subStr[0] == "O" 
                    or subStr[0] == "U" 
                ): vowels = vowels+1
                elif( 0 < len(subStr)): consonants = consonants +1
                
        if(consonants > vowels): 
            print("Stuart",consonants )
        elif(consonants < vowels): 
            print("Kevin",vowels )
        else: 
            print("Draw")
if __name__ == '__main__':