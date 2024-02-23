# This program fixes the problem in Part B, and instead of terminating the program after 10 or 20 digits, instead it
# does it until the repented of the arbitrary length is identified.


x = float(input("Please enter an float number bigger then 0 but less then 1: "))
# asks user to input an float number bigger then 0.
b = int(input("Please enter a base bigger then 1 but less then 17 : "))
# asks user to input a integer number between 1 - 17
List = ""
# This is an empty string, that will be used to add the results into.
duplicate = []
# This is an empty list, that will be used to add the repentend found in results.


# The 'character' user-defined function uses the chr function to find equivalent character of the 'remainder' given by
# the 'division' user-defined function. It returns the 'remainder' as a string that contains the character that is
# associated with the equivalent character code.


def character(integer):
    if integer in range(0, 10):     # If the integer (remainder) is between 0 - 9 the chr function is used to return the
                                    # the character of that 'remainder'
        return chr(48 + integer)    # 48 in the ASCII table is '0' so if the remainder was 9. 48 plus 9 would give us
                                    # '57'. 57 in the ASCII table is '9', so the value 9 would be returned.
    if integer in range(10, 16):  # If the integer (remainder) is between 10 - 15 the chr function is used to return the
                                  # the character of that 'remainder'
        return chr(55 + integer)  # 55 in the ASCII table is '0' so if the remainder was 10. 55 plus 10 would give us
                                  # '65'. 65 in the ASCII table is 'A', so the value A would be returned.


def repetend(decimal, base, results):  # the parameters decimal_number is 'n', base is 'b' and results is 'List'.
    while decimal % base == 0 and results not in duplicate: # The loop continues until decimal reaches 0 or if the
                                                            # the repentend is found.
        decimal = decimal * base
        remainder = decimal % base
        decimal = round(remainder, 4)
        remainder = int(remainder)
        results = results + character(remainder)
        results[remainder] = len(duplicate)                # This uses the len of result to store the repetend.
    print(x, "in base", b, "is:", results.rstrip('0') + ".", "Goodbye.", "ATTENTION! the repetend is ", duplicate)



repetend(x, b, List)
