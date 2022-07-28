def print_formatted(number):
    if(number > 0 and number < 100):
        i = 1
        padding = len(bin(number)[2:])
        while i <= number:
            print(str(i).rjust(padding), str(oct(i)[2:]).rjust(padding), str(
                hex(i)[2:]).upper().rjust(padding), str(bin(i)[2:]).rjust(padding))
            i = i + 1


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
