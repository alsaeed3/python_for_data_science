import sys


def main():
    # 1. Handle no arguements (Silent Exit)
    if len(sys.argv) < 2:
        return
    try:
        # 2. Handle too many arguements
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        # 3. Handle non-integer arguments
        try:
            num = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer") from None

        # 4. Even/Odd numbers checking logic
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except AssertionError as msg:
        print(f"Assertion Error: {msg}")


if __name__ == "__main__":
    main()
