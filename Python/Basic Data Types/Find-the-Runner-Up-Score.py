if __name__ == '__main__':
    def secondGreatestNumber(elements):
        maxElement = max(elements)
        secondGreatest = None
        for element in elements:
            if maxElement > element:
                if (secondGreatest is None):
                    secondGreatest = element
                elif(secondGreatest < element):
                    secondGreatest = element
        return secondGreatest

    n = int(input())

    if 2 <= n and n <= 10:

        def inputCheck(num):
            num = int(num)
            if -100 <= num and num <= 100:
                return num

        arr = map(inputCheck, input().split())
        elements = list(arr)

        if len(elements) == n:
            lessThanMax = secondGreatestNumber(elements)
            print(lessThanMax)
