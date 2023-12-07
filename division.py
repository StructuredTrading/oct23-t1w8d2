class NegativeError(Exception):
    pass


try:
    n = int(input("Enter a numerator: "))
    d = int(input("Enter a denominator: "))

    if n  < 0 or d < 0:
        raise Exception("No Negative Numbers Please.")

    q = n / d
    print(q)

except ZeroDivisionError as e:
    print(f"The program encounted a {e}.")

except ValueError as e:
    print(f"The program encounted a {e}.")

print("The end of the program.")