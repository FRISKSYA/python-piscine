import sys


def main():
    """Takes a string and counts upper, lower, punctuation, spaces, digits."""
    args = sys.argv[1:]

    if len(args) > 1:
        print("AssertionError: more than one argument is provided")
        return

    if len(args) == 1:
        text = args[0]
    else:
        print("What is the text to count?")
        text = sys.stdin.readline()

    upper = 0
    lower = 0
    punct = 0
    spaces = 0
    digits = 0

    for c in text:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isdigit():
            digits += 1
        elif c.isspace():
            spaces += 1
        elif c.isprintable():
            # punctuation = printable but not alnum and not space
            punct += 1

    total = len(text)
    print(f"The text contains {total} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    main()
