# This program takes two integers as input, This is then used to find its equivalent string representation in a
# different base.
# It takes the variable 'n' as the decimal number to be converted in the equivalent base, which is the variable 'b'.
# The input validation for this program uses try and except block to ensure that the code doesn't break if the incorrect
# input is provided.
# The 'character' user-defined function uses the chr function to find equivalent character of the 'remainder' given by
# the 'division' user-defined function. It returns the 'remainder' as a string that contains the character that is
# associated with the equivalent character code.
# The division function contains the main loop which will only stop until the variable 'n' is zero. In the loop the 'n'
# and 'b' is divided until zero is achieved. It also uses the modulo operator. It returns the remainder by dividing
# the operand in the left hand with the operand on the right hand. The remainder is then added to an empty list called
# 'List'. The 'List' is then printed with results of the decimal number 'n' in base 'b'.


List = ""                                     # This is an empty string, that will be used to add the results into.


# This part  of the program is the input validation, it makes sure that code doesn't break if the conditions are not met
# it instead ask the user to enter the input again.
# if conditions are met in try and except block the loop breaks and the input is accepted, if the conditions are
# never met the loop continues, and it will never stop until the right input is entered.


while True:                                   # This is an infinite loop.
    try:                                      # The try block checks for an error in the code.
        n = int(input("Please enter an integer number (>0): "))  # asks user to input a number bigger then 0.
        while n < 1:                          # This only executes the statement, when the condition ( n<1) is true.
            print("Invalid Input")            # If a number smaller than 1 is entered. 'Invalid Input' is printed.
            n = int(input("Please enter an integer number (>0) : "))  # ask user to enter again.
    except ValueError:                        # The except block deals with the 'ValueError' error.
        print("Invalid Input")                # When value entered is not an integer number, 'Invalid Input' is printed.
    else:                                     # This statement is executed if the above conditions aren't required.
        break                                 # This breaks the loop.
while True:
    try:
        b = int(input("Please enter a base between 2 and 16 : "))
        while b < 2 or b > 16:         # This only executes the statement, when the condition (b < 2 or b > 16) is true.
            print("Invalid Input")     # If a number entered isn't between 2 and 16 .'Invalid Input' is printed.
            b = int(input("Please enter a base between 2 and 16  : "))
    except ValueError:
        print("Invalid Input")
    else:
        break


# The 'character' user-defined function uses the chr function to find equivalent character of the 'remainder' given by
# the 'division' user-defined function. It returns the 'remainder' as a string that contains the character that is
# associated with the equivalent character code.


def character(integer):
    if integer in range(0, 10):     # If the integer (remainder) is between 0 - 9 the chr function is used to return the
                                    # the character of that 'remainder'
        return chr(48 + integer)    # 48 in the ASCII table is '0' so if the remainder is 9. 48 plus 9 would give us
                                    # '57'. 57 in the ASCII table is '9', so the value 9 would be returned.
    if integer in range(10, 16):  # If the integer (remainder) is between 10 - 15 the chr function is used to return the
                                  # the character of that 'remainder'
        return chr(55 + integer)  # 55 in the ASCII table is '0' so if the remainder is 10. 55 plus 10 would give us
                                  # '65'. 65 in the ASCII table is 'A', so the value A would be returned.


# MAIN LOOP - it uses the modulo operator to find the reminder, and adds 'reminder' to the empty list 'List'.
# integer division is used to get the next 'n' which is used to get the 'reminder'. This loop runs until 'n' is zero.


def division(decimal_number, base, result):   # the parameters decimal_number is 'n', base is 'b' and results is 'List'.
    while decimal_number is not 0:            # The while statement will run until the 'decimal_number' is zero.
        remainder = decimal_number % base     # this statement finds the reminder by using modulo operand.
                                              # And creates new variable named 'remainder'.
                                              # The results of this operation is then stored in 'remaninder'.
        result = character(remainder) + result # It calls the 'character' function to return the appropriate character
                                            # for integer value in 'remainder'. The value is then stored in the 'List'.
        decimal_number = decimal_number // base  # This statement uses integer division to divide the decimal number
                                                # with the base to give, a new integer value which will be the replace
                                                # the old value in 'decimal_number' is replaced to a new integer value.
    print(n, "in base", b, "is:", result + ".", "Goodbye.")  # This prints the 'result' for example it will print,
                                                # 467(n) in base 12(b) is : 32B(results). Goodbye.


division(n, b, List)  # This calls the division function.
