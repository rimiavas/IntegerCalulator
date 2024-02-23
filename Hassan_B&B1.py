# This program takes the users input of 'b' and 'x' which used to convert float into its equivalent string
# representation in any given base the solution works by taking users input of b and x and creating a while loop for
# decimal and base to be multiplied and for remainder to be found using modulo operand. The 'character' user-defined
# function uses the chr function to find equivalent character of the 'remainder' given by the 'division' user-defined
# function. It returns the 'remainder' as a string that contains the character that is associated with the equivalent
# character code. the variable 'remainder' calls the character function to find the appropriate character for the
# remainder to then be added to the empty list, 'List'. The round function is used to round float values to 4 decimal
# places and the  variable 'digits' is  used as a counter. The 'remainder' then is  converted from a float into
# integer.  The 'List' is then printed with results of the decimal 'n' in base 'b' prints the results where there's
# no trailing zeros due to the use of .rstrip .


List = "."  # empty list is used for the results to be added.
x = float(input(
    "Please enter an float number bigger then 0 but less then 1: "))  # user input x is less than one, so it's a float
b = int(input(
    "Please enter a base bigger then 1 but less then 17 : "))  # user input b is integer as base number needs to be


# between 1-17


# this user defined function takes the integer and finds the corresponding character or number
def character(integer):
    if integer in range(0, 10):  # If the integer (remainder) is between 0 - 9 the chr function is used to return the
        # the character of that 'remainder'
        return chr(48 + integer)  # 48 in the ASCII table is '0' so if the remainder is 9. 48 plus 9 would give us
        # '57'. 57 in the ASCII table is '9', so the value 9 would be returned.
    if integer in range(10, 16):  # If the integer (remainder) is between 10 - 15 the chr function is used to return the
        # the character of that 'remainder'
        return chr(55 + integer)  # 55 in the ASCII table is '0' so if the remainder is 10. 55 plus 10 would give us
        # '65'. 65 in the ASCII table is 'A', so the value A would be returned.


# MAIN LOOP  this loop finds the reminder and adds it to the list .This loop will end when digits reach 20.It uses
# multiplication to find the next decimal value and uses modulo operand to add the remainder to the list.
def converting_decimals(decimal, base, results):
    digits = 0  # this is a counter
    while digits != 20:  # this statement will run until digits reaches 20
        decimal = decimal * base  # using multiplication (decimal*base) it replaces the old value of decimal and
        # stores a new one
        remainder = decimal % base  # new variable called remainder is (decimal%base)
        decimal = round(remainder, 4)  # this function rounds float value to 4 decimal places
        remainder = int(remainder)  # new assignment of remainder converts float into integer
        results = results + character(
            remainder)  # this is where remainder is added to the list and the character function is called to return
        # appropriate character for the integer value this is then stored in the list
        digits = digits + 1  # counter incrementing by 1 every loop

    print(x, "in base", b, "is:", results.rstrip('0') + ",",
          "Goodbye.")  # this prints the results where there's no trailing zeros due to the use of .rstrip


converting_decimals(x, b, List)  # this calls the converting_decimals function.
