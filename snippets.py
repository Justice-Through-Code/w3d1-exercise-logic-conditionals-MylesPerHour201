
'''
Debug the following code snippets so that they all run successfully
'''


def snippet_1():
    u = 5
    v = 2

    if u * v == 10:
        print(f"The product of u ({u}) and v ({v}) is 10")
    else:
        print(f"The product of u ({u}) and v ({v}) is not 10")


def snippet_2():
    x = 15
    y = 25

    z = 30

    if z < x:
        print("z is less than x")

    elif z > x and z < y:
        print("z is between x and y")

    else:
        print("z is greater than y")


def snippet_3():
    # TODO: Modify the comparison operator below so the `assert` statement passes
    # TODO: Update the print statement to reflect the fact that a 'is equal to' b

    a = 1
    b = 1
    c = (a == b)

    print(f"The value of c ({c}) is True since a ({a}) is equal to b ({b}).")
    assert(c == True)  # <-- DO NOT EDIT THIS LINE

    # c = (a >= b)
    # print(f"The value of c ({c}) is True since a ({a}) is greater than or equal to b ({b}).")
    # CAN YOU PLEASE CONFIRM THAT, WHILE THIS CODE DOES NOT PASS UNITTEST, IT IS TECHNICALLY TRUE AND PASSES THE ASSERT STATEMENT (c == True)


def snippet_4():
    # TODO: Modify exactly one boolean operator in the assignment of d, so that d evaluates to False

    d = (5 < 7) and not (8 < 20)
    # with "and not" in order for d to run as True, the first statement must be True and the second statement must be False. Since the second statement is True, d runs as False 

    # TODO: Explain how d is set to False in a comment
    assert(d == False)  # <-- DO NOT EDIT THIS LINE


def snippet_5():
    # TODO: Modify the comparison operator so o evalutes to true
    # TODO: Update the print statement to reflect the changes

    m = "GOAT"
    n = "goat"

    o = (m != n)

    print (f"The value of o ({o}) is True since Python is case-sensitive.")
    assert(o == True)  # <-- DO NOT EDIT THIS LINE
