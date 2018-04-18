"""
Exam 2, problem 4.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Zhengxiao Zou.  April 2018.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    # -------------------------------------------------------------------------
    # Uncomment the following calls to the testing functions one at a time
    # as you work the problems.
    # -------------------------------------------------------------------------
    print('Un-comment the calls in MAIN one by one')
    print(' to run the testing code as you complete the TODOs.')

    run_test_problem4a()
    run_test_problem4b()


###############################################################################
# DONE: 2.  READ the doc-string for the   is_prime   function below.
#           It is the same  is_prime  function that you have used previously,
#           except that it returns  False  for all integers less than 2.
#
#   ***          Throughout these problems,           ***
#   *** you must CALL functions wherever appropriate. ***
#
#   Once you are confident that you understand the contents of this comment,
#   change the TO-DO for this problem to DONE.
###############################################################################
def is_prime(n):
    """
    What comes in:  An integer.
    What goes out:
      -- Returns True if the given integer is prime, else returns False.
         All integers less than 2 are treated as NOT prime.
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
      -- is_prime(0)  returns  False
    Note: The algorithm used here is simple and clear but slow.
    """
    if n < 2:
        return False
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True


def run_test_problem4a():
    """ Tests the   problem4a   function. """
    ###########################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    # You may add more tests if you wish, but you are not required to do so.
    ###########################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the  problem4a  function:')
    print('--------------------------------------------------')

    format_string = '    problem4a( {} )'
    passed_tests = 0

    # Test 1:
    print()
    print('Test 1:')
    strings = ['Nope', '', 'Hello', 'Goodbye', 'More stuff']

    expected = 'Hello'
    print('  This test case calls:')
    print(format_string.format(strings))
    print("  Expected:", expected)

    actual = problem4a(strings)
    print("  Actual:  ", actual)
    result = print_result_of_test(expected, actual)
    passed_tests = passed_tests + result

    # Test 2:
    print()
    print('Test 2:')
    strings = ['SixSix', 'I am nine', 'This', 'is definitely fun!']

    expected = -1
    print('  This test case calls:')
    print(format_string.format(strings))
    print("  Expected:", expected)

    actual = problem4a(strings)
    print("  Actual:  ", actual)
    result = print_result_of_test(expected, actual)
    passed_tests = passed_tests + result

    # Test 3:
    print()
    print('Test 3:')
    strings = ('01234567', '0123456789', '0123', '0123456')

    expected = '0123456'
    print('  This test case calls:')
    print(format_string.format(strings))
    print("  Expected:", expected)

    actual = problem4a(strings)
    print("  Actual:  ", actual)
    result = print_result_of_test(expected, actual)
    passed_tests = passed_tests + result

    if passed_tests == 3:
        testing_helper.print_colored('\n*** PASSED all 3 tests! Good! ***',
                                     color='blue')
    else:
        testing_helper.print_colored('\n*** FAILED at least one test! ***',
                                     color='red')


def problem4a(strings):
    """
    What comes in:  A sequence of strings.
    What goes out:
       Returns the first string in the sequence whose length is prime,
       or -1 if there is no string in the sequence whose length is prime.
    Side effects: None.
    Examples:

      problem4a(['Nope', '', 'Hello', 'Goodbye', 'More stuff'])
        returns  'Hello'
            because:
            -- the length of 'Nope' is 4 (which is NOT prime)
            -- the length of the empty string is 0 (which is NOT prime), and
            -- the length of 'Hello' is 5 (which IS prime)

      problem4a(['SixSix', 'I am nine', 'This', 'is definitely fun!'])
        returns  -1
             because the lengths of the strings are 6, 9, 4, and 18,
             respectively, none of which are prime.

      problem4a(('01234567', '0123456789', '0123', '0123456'))
        returns '0123456'
             because the lengths of the strings are 8, 10, 4, and 7,
             respectively, only the last of which is prime.

    Type hints:
      :type [str]
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------
    size = len(strings)
    print(size)
    for k in range (size):
        target = strings[k]
        letter = target.__sizeof__()
        print(letter-49)
        answer = is_prime(letter-49)
        if answer == True:
            return strings[k]
    return -1



def run_test_problem4b():
    """ Tests the   problem4b   function. """
    ###########################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    # You may add more tests if you wish, but you are not required to do so.
    ###########################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the  problem4b  function:')
    print('--------------------------------------------------')

    format_string = '    problem4b( {} )'
    passed_tests = 0

    # Test 1:
    print()
    print('Test 1:')
    seq = [('SixSix', 'I am nine', 'This', 'is definitely fun!'),
                  ('Nope', '', 'Hello', 'Goodbye', 'More stuff'),
                  ('', 'This is seventeen', 'abc'),
                  ('none', 'here')]

    expected = True
    print('  This test case calls:')
    print(format_string.format(seq))
    print("  Expected:", expected)

    actual = problem4b(seq)
    print("  Actual:  ", actual)
    result = print_result_of_test(expected, actual)
    passed_tests = passed_tests + result

    # Test 2:
    print()
    print('Test 2:')
    seq = [('SixSix', 'I am nine', 'This', 'is definitely fun!'),
                  ('Nope', 'even', 'not prime'),
                  ('', 'This is eighteen!!', '1234567890'),
                  ('none', 'here')]

    expected = False
    print('  This test case calls:')
    print(format_string.format(seq))
    print("  Expected:", expected)

    actual = problem4b(seq)
    print("  Actual:  ", actual)
    result = print_result_of_test(expected, actual)
    passed_tests = passed_tests + result

    if passed_tests == 2:
        testing_helper.print_colored('\n*** PASSED all 2 tests! Good! ***',
                                     color='blue')
    else:
        testing_helper.print_colored('\n*** FAILED at least one test! ***',
                                     color='red')


# -----------------------------------------------------------------------------
#    *** IMPORTANT:  THIS PROBLEM COUNTS ONLY 2 POINTS
#                    AND HAS AN ELEGANT SOLUTION.  DO NOT GET STUCK ON IT!
# -----------------------------------------------------------------------------
def problem4b(list_of_tuples_of_strings):
    """
    What comes in:  A list of tuples of strings.
    What goes out:
       Returns True if there is any string in the list of tuples of strings
       whose length is prime.
    Side effects: None.
    Examples:
      problem4b( [('SixSix', 'I am nine', 'This', 'is definitely fun!'),
                  ('Nope', '', 'Hello', 'Goodbye', 'More stuff'),
                  ('', 'This is seventeen', 'abc'),
                  ('none', 'here')] )
        returns  True
             because it DOES have strings whose lengths are prime
             (namely, 'Hello', 'Goodbye', 'This is seventeen', and 'abc')

      problem4b( [('SixSix', 'I am nine', 'This', 'is definitely fun!'),
                  ('Nope', 'even', 'not prime'),
                  ('', 'This is eighteen!', '1234567890'),
                  ('none', 'here')] )
         returns  False
         because the lengths of the strings are
            6, 9, 4, 18, 4, 4, 9, 0, 18, and 10, respectively,
         none of which are prime.

    Type hints:
      :type [str]
    """
    # -------------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #          Tests have been written for you (above).
    #    *** IMPORTANT:  THIS PROBLEM COUNTS ONLY 2 POINTS
    #                    AND HAS AN ELEGANT SOLUTION.  DO NOT GET STUCK ON IT!
    # -------------------------------------------------------------------------
    holder = 1
    str = list_of_tuples_of_strings
    size = len(list_of_tuples_of_strings)
    for k in range (size):
        target = str[k]
        if problem4a(target) == -1:
            x = 1
        else: return True
    return False



###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_result_of_test(expected, actual):
    return testing_helper.print_result_of_test(expected, actual)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    time.sleep(1)
    raise
