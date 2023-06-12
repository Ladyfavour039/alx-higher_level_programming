#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add
    from calculator_1 import sub
    from calculator_1 import mul
    from calculator_1 import div

    a = 10
    b = 5

    print(a, "+", b, "=", add(a, b))
    print(a, "-", b, "=", sub(a, b))
    print(a, "*", b, "=", mul(a, b))
    print(a, "/", b, "=", round(div(a, b)))
