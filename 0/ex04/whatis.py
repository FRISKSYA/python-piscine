import sys

args = sys.argv[1:]

if len(args) == 0:
    pass
elif len(args) > 1:
    print("AssertionError: more than one argument is provided")
else:
    try:
        n = int(args[0])
    except ValueError:
        print("AssertionError: argument is not an integer")
    else:
        if n % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
