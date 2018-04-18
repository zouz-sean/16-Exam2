"""
Exam 1, problem 2.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Zhengxiao Zou.  March 2018.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
import testing_helper


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem2()


def run_test_problem2():
    """ Tests the  problem2   function. """
    ###########################################################################
    # THESE TESTS ARE ALREADY DONE.  DO NOT CHANGE THEM.
    ###########################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2   function:')
    print('--------------------------------------------------')

    format_string = '    problem2a( {}, {} )'
    passed_tests = 0

    # Test 1:
    print()
    print('Test 1:')
    n = 10
    sequence = [9, 15, 2, 20, 13, 6, 8, 1, 17]

    expected = [9, 2, 6]
    print('  This test case calls:')
    print(format_string.format(n, sequence))
    print("  Expected:", expected)

    actual = problem2(n, sequence)
    print("  Actual:  ", actual)
    result = print_result_of_test(expected, actual)
    passed_tests = passed_tests + result

    # Test 2:
    print()
    print('Test 2:')
    n = 7
    sequence = [9, 15, 2, 20, 13, 6, 8, 1, 17]

    expected = [2, 6, 1]
    print('  This test case calls:')
    print(format_string.format(n, sequence))
    print("  Expected:", expected)

    actual = problem2(n, sequence)
    print("  Actual:  ", actual)
    result = print_result_of_test(expected, actual)
    passed_tests = passed_tests + result

    # Test 3:
    print()
    print('Test 3:')
    n = 5
    sequence = [9, 15, 2, 20, 13, 6, 8, 1, 17]

    expected = 'Too few'
    print('  This test case calls:')
    print(format_string.format(n, sequence))
    print("  Expected:", expected)

    actual = problem2(n, sequence)
    print("  Actual:  ", actual)
    result = print_result_of_test(expected, actual)
    passed_tests = passed_tests + result

    # Test 4:
    print()
    print('Test 4:')
    n = 5
    sequence = [5, 4, 11, 2, 4, 4]

    expected = [4, 2, 4]
    print('  This test case calls:')
    print(format_string.format(n, sequence))
    print("  Expected:", expected)

    actual = problem2(n, sequence)
    print("  Actual:  ", actual)
    result = print_result_of_test(expected, actual)
    passed_tests = passed_tests + result

    # Test 5:
    print()
    print('Test 5:')
    n = 8
    sequence = [100, 100]

    expected = 'Too few'
    print('  This test case calls:')
    print(format_string.format(n, sequence))
    print("  Expected:", expected)

    actual = problem2(n, sequence)
    print("  Actual:  ", actual)
    result = print_result_of_test(expected, actual)
    passed_tests = passed_tests + result

    # Test 6:
    print()
    print('Test 6:')
    n = 10
    sequence = [1, 2]

    expected = 'Too few'
    print('  This test case calls:')
    print(format_string.format(n, sequence))
    print("  Expected:", expected)

    actual = problem2(n, sequence)
    print("  Actual:  ", actual)
    result = print_result_of_test(expected, actual)
    passed_tests = passed_tests + result

    if passed_tests == 6:
        testing_helper.print_colored('\n*** PASSED all 6 tests! Good! ***',
                                     color='blue')
    else:
        testing_helper.print_colored('\n*** FAILED at least one test! ***',
                                     color='red')


def problem2(n, seq):
    """
    What comes in:
      -- An integer  n  and a sequence of integers.
    What goes out:
      -- Returns a list containing the first three numbers in the sequence
           that are strictly less than the given N, unless the sequence has
           fewer than three numbers strictly less than N,
           in which case the function returns the string 'Too few'.
    Side effects:  None.
    Examples:
      problem2( 10, [9, 15, 2, 20, 13, 6, 8, 1, 17] )    returns [9, 2, 6]
      problem2( 10, [9, 15, 2, 20, 13, 6, 8, 1, 17] )    returns [2, 6, 1]
      problem2( 10, [9, 15, 2, 20, 13, 6, 8, 1, 17] )    returns 'Too few'
      problem2( 5,  [5, 4, 11, 2, 4, 4] )                returns [4, 2, 4]
      problem2( 8,  [100, 100] )                         returns 'Too few'
      problem2( 8,  [1, 2] )                             returns 'Too few'

    Type hints
      :type n:    int
      :type seq:  [int]
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------
    size = len(seq)
    threshold = n
    result = []
    count  = 0
    for k in range (size):
        if seq[k] < threshold:
            result.append(seq[k])
            count = count + 1
            if count == 3:
                break
    if count < 3:
        return 'Too few'
    return result



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
