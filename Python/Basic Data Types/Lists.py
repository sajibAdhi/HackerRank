if __name__ == '__main__':
    N = int(input())

    newList = list()
    count = 0

    while(True):

        if (count < N):
            operation = input().split()

            if (operation[0] == "insert"):
                newList.insert(int(operation[1]), int(operation[2]))
            elif (operation[0] == "print"):
                print(newList)
            elif (operation[0] == "remove"):
                newList.remove(int(operation[1]))
            elif (operation[0] == "append"):
                newList.append(int(operation[1]))
            elif (operation[0] == "sort"):
                newList.sort()
            elif (operation[0] == "pop"):
                newList.pop()
            elif (operation[0] == "reverse"):
                newList.reverse()
            else:
                break
            count = count + 1
        else:
            break
