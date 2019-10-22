# Scope
Write a program that calculates the amount of money a person would earn over a period of time if his or her salary is one penny the first day, two pennies the second day, and continues to double each day. The program should ask the user for the number of days. Display a table showing what the salary was for each day, then show the total pay at the end of the period. The output should be displayed in a dollar amount, not the number of pennies.

### Example Run
    Enter the number of days:  20
    Day	            Pennies
    -------------------------
    1 	             $ 0.01
    2 	             $ 0.02
    3 	             $ 0.04
    4 	             $ 0.08
    5 	             $ 0.16
    6 	             $ 0.32
    7 	             $ 0.64
    8 	             $ 1.28
    9 	             $ 2.56
    10 	             $ 5.12
    11 	            $ 10.24
    12 	            $ 20.48
    13 	            $ 40.96
    14 	            $ 81.92
    15 	           $ 163.84
    16 	           $ 327.68
    17 	           $ 655.36
    18 	          $ 1310.72
    19 	          $ 2621.44
    20 	          $ 5242.88
    The total salary for 20 days is: $ 10485.75

# Pseudocode
    START
    Set pennies = 0
    Set value = 0.0
    Set total = 0.0
    prompt user for number of days
    Print header
      Day	              Pennies
      -------------------------
    FOR each day starting at 1
      value = pennies / 100
      print day and value
      pennies = pennies * 2
      total = total + value
    Print total salary
    END
