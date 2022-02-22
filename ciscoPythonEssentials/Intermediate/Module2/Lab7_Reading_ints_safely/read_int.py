#!/usr/bin/python
"""
The task is:
write a function able to input integer values and check if they are within a specified range.

The function should:

* accept three arguments: a prompt, a low acceptable limit, and a high acceptable limit;

* if the user enters a string that is not an integer value, the function should emit the
message Error: wrong input, and ask the user to input the value again;

* if the user enters a number which falls outside the specified range, the function should
emit the message Error: the value is not within permitted range (min..max) and ask the user
to input the value again;

* if the input value is valid, return it as a result.
"""

def read_int(prompt, min, max):
    is_valid = False

    while not is_valid:
        try:
            user_number = int(input(prompt))
            assert min < user_number < max
            is_valid = True
        except (ValueError, NameError):
            print("Error: wrong input.")
        except AssertionError:
            print(f"Error: the value {user_number} is not within permitted range ({min} .. {max}).")

    return user_number

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
