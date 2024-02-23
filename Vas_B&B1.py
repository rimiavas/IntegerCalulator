List = "."
x = float(input("Please enter an float number bigger then 0 but less then 1: "))
b = int(input("Please enter a base bigger then 1 but less then 17 : "))


def character(integer):
    if integer in range(0, 10):
        return chr(48 + integer)
    if integer in range(10, 16):
        return chr(55 + integer)

def decimaltobinary(decimal, base, results):
    digits = 0
    while digits != 20:
        decimal = decimal * base
        remainder = decimal % base
        decimal = round(remainder, 4)
        remainder = int(remainder)
        results = results + character(remainder)
        digits = digits + 1

    print(x, "in base", b, "is:", results.rstrip('0') + ".", "Goodbye.")


decimaltobinary(x, b, List)
