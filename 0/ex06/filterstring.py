import sys
from ft_filter import ft_filter


def main():
    """Filters words in a string by length greater than N."""
    args = sys.argv[1:]

    try:
        assert len(args) == 2
        s = args[0]
        n = int(args[1])
        assert isinstance(s, str)
    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")
        return

    result = ft_filter(lambda word: len(word) > n, s.split(" "))
    print(result)


if __name__ == "__main__":
    main()
