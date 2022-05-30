'''Assignment 1

This assignment covers your basic profiency with
    Python. It engages your ability to transform
    data without affecting anything outside the program.

This assignment places heavy emphasis on basic Python constructs.
'''

from ast import Return


def factorial(x):
    '''Item 1. 
    Factorial. 1 point.
    
    Returns the factorial of an integer.
    An integer's factorial is the product of the integer and all
        integers below it.

    Parameters
    ----------
    x: int
        the integer whose factorial to return

    Returns
    -------
    integer
        the factorial of the argument
    '''
    # Write your code below this line
    
    factorial = 1
    if int(x) >= 1:
        for i in range (1,int(x)+1):
            factorial = factorial * i
    print("Factorial of ",x , " is : ",factorial)
    return factorial
x = input("Enter a number: ")
factorial(x)


def classify_grade(number_grade):
    '''Item 2.
    Classify Grade. 2 points.
    
    Returns the letter grade equivalent of a number grade.
    For this item, use these letter grade buckets:
        A: 92-100
        B+: 86-91.9
        B: 80-85.9
        C+: 74-79.9
        C: 67-73.9
        D: 60-66.9
        F: 0-59.9

    Parameters
    ----------
    number_grade: float
        the number grade to convert into a letter grade.

    Returns
    -------
    str
        the letter grade equivalent of the number grade.
    '''
    # Write your code below this line
    classify_grade = 1
    if int(number_grade)<60:
        classify_grade = "F"
    elif int(number_grade)<67:
        classify_grade = "D"
    elif int(number_grade)<74:
        classify_grade = "C"
    elif int(number_grade)<80:
        classify_grade = "C+"
    elif int(number_grade)<86:
        classify_grade = "B"
    elif int(number_grade)<92:
        classify_grade = "B+"
    else:
        classify_grade = "A"
    print("Your Grade is: ",classify_grade)
    Return
number_grade = int(input("Enter Grade: "))
classify_grade(number_grade)

def average_weight(item_quantity_1, item_weight_1, item_quantity_2, item_weight_2):
    '''Item 3.
    Average Weight. 3 points.
    
    You have purchased two bags of items. 
    The first bag contains one type of item, and the second bag contains another type.
    Return the weighted average weight of the items.
        
    Parameters
    ----------
    item_quantity_1: int
        the quantity of items in the first bag.
    item_weight_1: float
        the weight of each individual item in the first bag.
    item_quantity_2: int
        the quantity of items in the second bag.
    item_weight_2: float
        the weight of each individual item in the second bag.

    Returns
    -------
    float
        the weighted average weight of one item.
    '''
    # Write your code below this line

def string_sum(string):
    '''Item 4.
    String Sum. 3 points.
    
    Returns the sum of the digits provided in a string.
    For this item:
        1. Sum the digits contained in the string.
        2. Ignore any non-digit characters contained in the string.

    Parameters
    ----------
    string: str
        a string that can contain any character.

    Returns
    -------
    int
        the sum of the digits contained in the string.
    '''
    # Write your code below this line
    sum_digit = 0
    for x in string:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z

    return sum_digit
     
print(string_sum("123abcd45"))
print(string_sum("abcd1234"))


def distance(x_1, y_1, x_2, y_2):
    '''Item 5.
    Distance. 3 points.

    Returns the distance between two points.
    To get the distance between two points:
        1. Get the difference between the two x-coordinates
        2. Get the difference between the two y-coordinates
        3. Sum the previous two values
        4. Return the square root of the sum

    You may want to import the `math` library for this number.

    Parameters
    ----------
    x_1: float
        the first x-coordinate
    y_1: float
        the first y-coordinate
    x_2: float
        the second x-coordinate
    y_2: float
        the second y-coordinate

    Returns
    -------
    float
        the distance between the two coordinates
    '''
    # Write your code below this line
    d1 = (x_2 - x_1)**2
    d2 = (y_2 - y_1)**2
    s1 = (d1 + d2)**0.5
    return(float(s1))

def make_change(amount):
    '''Item 6.
    Make Change. 5 points.
    
    Return the combination of coins needed to make change for the given amount,
        which is given in centavos.
    For this item:
        1. You can return 1 peso, 25 centavos, 10 centavos, 5 centavos, and 1 centavo coins.
        2. Use the minimum number of coins possible.

    Parameters
    ----------
    amount: int
        the amount, in centavos, to make change for.

    Returns
    -------
    str
        the string representation of the change to be given.
        Format it like this:
            "1P:{amount}/25C:{amount}/10C:{amount}/5C:{amount}/1C:{amount}"
    '''
    # Write your code below this line
    amt = amount * 100
    amt1 = int(amt//100)
    amt = amt%100
    amt2 = int(amt//25)
    amt = amt%25
    amt3 = int(amt//10)
    amt = amt%10
    amt4 = int(amt//5)
    amt = amt%5
    amt5 = int(amt//1)
    return("1P:{"+str(amt1)+"}/25C:{"+str(amt2)+"}/10C:{"+str(amt3)+"}/5C:{"+str(amt4)+"}/1C:{"+str(amt5)+"}")