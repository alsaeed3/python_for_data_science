import sys


def main():
    """
    Counts upper, lower, punctuation, spaces, and digits in a string.
    """
    try:
        # 1. Handle Argument Logic
        if len(sys.argv) < 2:
            try:
                print("What is the text to count?")
                text = sys.stdin.readline()
            except EOFError:
                return
        elif len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        else:
            text = sys.argv[1]

        # 2. Define Punctuation Marks
        punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

        # 3. Initialize Counters
        counts = {
            "upper": 0,
            "lower": 0,
            "punc": 0,
            "space": 0,
            "digit": 0
        }

        # 4. Counting Loop
        for char in text:
            if char.isupper():
                counts["upper"] += 1
            elif char.islower():
                counts["lower"] += 1
            elif char.isspace():
                counts["space"] += 1
            elif char.isdigit():
                counts["digit"] += 1
            elif char in punctuation:
                counts["punc"] += 1

        # 5. Output Results
        print(f"The text contains {len(text)} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punc']} punctuation marks")
        print(f"{counts['space']} spaces")
        print(f"{counts['digit']} digits")

    except AssertionError as msg:
        print(f"AsserionError: {msg}")


if __name__ == "__main__":
    main()
