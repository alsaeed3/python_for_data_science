"""Module for filtering words in a string by minimum length."""
import sys
from ft_filter import ft_filter


def main():
    """
    Filters words in a string by minimum length.
    """
    try:
        # 1. Handle Argument Logic - check count first
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]
        if not isinstance(text, str):
            raise AssertionError("the arguments are bad")

        # Convert second argument to int
        try:
            length_limit = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad") from None

        # 2. Filter Logic - split into words and filter by length
        words = text.split()
        filtered_words = list(
            ft_filter(lambda word: len(word) > length_limit, words))
        print(filtered_words)

    except AssertionError as msg:
        print(f"AssertionError: {msg}")


if __name__ == "__main__":
    main()
