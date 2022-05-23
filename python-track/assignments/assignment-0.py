'''Assignment 0

This assignment is a giveaway assignment.
By completing this assignment, you will familiarize yourself with this
    course's submission mechanics.
'''

from audioop import avg


def three_number_average(x, y, z):
    '''Item 1.
    Three Number Average. 3 points.

    Returns the average of three numbers.

    Parameters
    ----------
    x: int
        the first number
    y: int
        the second number
    z: int
        the third number

    Returns
    -------
    float
        the average of x, y, and z
    '''
    # Write your code below this line
    three_number_average = (x+y+z)/3
    print(three_number_average)
    return three_number_average
x=int(input())
y=int(input())
z=int(input())
three_number_average(x,y,z)
