if __name__ == '__main__':
    n = int(input())

    if 2 <= n and n <= 10:

        def inputCheck(num):
            num = int(num)
            if -100 <= num and num <= 100:
                return num

        arr = map(inputCheck, input().split())
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
