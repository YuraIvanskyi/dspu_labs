import math
import random


def print_table(rows: list[list[str]]) -> str:
    for row in rows:
        row_text = " | ".join(f"{column:^20}" for column in row)
        print(row_text)
        print("-" * (len(row_text)))


def task_1():
    print("Task 1: Function approximation and whatever")
    a, b, h, n = map(float, input("Enter a, b, h, n, separated by whitespace: ").split())
    print(f"{a=}, {b=}, {h=}, {n=}")

    def _y_x(x: float) -> float:
        return math.cos(x)

    def _s_x(x: float, n: int) -> float:
        return sum([(((math.pow(-1, i)))) * ((x ** (2 * i)) / math.factorial(2 * i)) for i in range(n + 1)])

    headers = ["x", "Y(x)", "S(x)", "|Y(x) - S(x)|"]
    results = []
    x = a
    while a <= x <= b + h:
        y_x = round(_y_x(x), 10)
        s_x = round(_s_x(x, int(n)), 10)
        diff = round(abs(_y_x(x) - _s_x(x, int(n))), 10)
        results.append([round(x, 10), y_x, s_x, diff])
        x += h

    print_table([headers, *results])


def task_2():
    print("Task 2: 2 Functions values on a given interval")
    a, b, n = -2, 5, 14
    print(f"My task: {a=}, {b=}, {n=}")
    headers = ["x", "f1(x)", "f2(x)"]

    def f1(x: float) -> float:
        return abs(x + 10) ** 5

    def f2(x: float) -> float:
        return math.e ** (-1 * (x + 5))

    def _by_for_loops():
        results = []
        step = (b - a) / (n - 1)
        for i in range(n):
            x = a + i * step
            results.append([x, round(f1(x), 10), round(f2(x), 10)])
        return results

    def _by_while_loop():
        results = []
        x, step = a, (b - a) / n
        while x <= b + step:
            results.append([x, round(f1(x), 10), round(f2(x), 10)])
            x += step
        return results

    print("Results by while loop:")
    print_table([headers, *_by_while_loop()])
    print("\nResults by for loop:")
    print_table([headers, *_by_for_loops()])


def task_3():
    print("Task 3: Functions values on a given interval with conditions")
    a, b, h = map(float, input("Enter a, b, h, separated by whitespace: ").split())
    print(f"{a=}, {b=}, {h=}")
    results = []
    x = a
    while a <= x <= b:
        partial_result = 2 + 6 * x
        if x <= 0:
            partial_result += math.log1p(math.cos(x)) + x**5
        elif 0 < x <= 3:
            partial_result += 1 / math.tan((1 + math.log1p(x) / 3))
        else:
            partial_result += 12 * x - x**8
        results.append([round(x, 10), round(partial_result, 10)])
        x += h

    print_table([["All results:"], ["x", "f(x)"], *results])


def task_4():
    print("Task 4: Graphical representation of function")
    print("Image should be seen to know what it is about")
    R, a, b, h = map(float, input("Enter R, a, b, h, separated by whitespace: ").split())
    print(f"{R=}, {a=}, {b=}, {h=}")
    results = []
    x = a
    while a <= x <= b:
        if x <= -R:
            results.append([round(x, 10), round(R, 10)])
        elif -R < x < R:
            results.append([round(x, 10), round(-1 * math.sqrt(R**2 - x**2), 10)])
        elif R <= x <= 6:
            results.append([round(x, 10), round(R + ((-3 - R) / (6 - R)) * (x - R), 10)])
        elif x > 6:
            results.append([round(x, 10), round(x - 9, 10)])
        x += h

    print_table([["All results:"], ["x", "f(x)"], *results])


def task_5():
    print("Task 5: Coordinate target shooting")
    R = float(input("Enter R: "))
    print(f"{R=}")

    def __condition(x: float, y: float) -> bool:
        return (
            -R <= x <= R
            and -R <= y <= R
            and (x + R) ** 2 + (y - R) ** 2 >= R**2
            and (x - R) ** 2 + (y + R) ** 2 >= R**2
        )

    for i in range(1, 11):
        x, y = map(float, input(f"Enter coordinates for attempt {i}: ").split())
        if __condition(x, y):
            print(f"({x=},{y=}) Shot: Target hit! Attempt {i}")
        else:
            print(f"({x=},{y=}) Shot: Target missed! Attempt {i}")

    for i in range(11, 21):
        x, y = random.uniform(-2 * R, 2 * R), random.uniform(-2 * R, 2 * R)
        if __condition(x, y):
            print(f"({x=},{y=}) Shot: Target hit by random! Attempt {i}")
        else:
            print(f"({x=},{y=}) Shot: Target missed by random! Attempt {i}")


def task_6():
    """why... I'd rather do this properly..."""
    print("Task 6: 4 method looping function")

    def _method_1() -> float:
        """for ... for loops"""
        product = 1
        for i in range(1, 11):
            nominator = i
            for k in range(1, i + 1):
                nominator += 1 / k
            denominator = 0
            for k in range(1, i + 1):
                denominator += 1 / k
            product *= nominator / math.sqrt(denominator)
        return product

    def _method_2() -> float:
        """for ... while... loops"""
        product = 1
        for i in range(1, 11):
            nominator = i
            k = 1
            while k <= i:
                nominator += 1 / k
                k += 1
            denominator = 0
            k = 1
            while k <= i:
                denominator += 1 / k
                k += 1
            product *= nominator / math.sqrt(denominator)
        return product

    def _method_3() -> float:
        """while... for... loops"""
        product = 1
        i = 1
        while i <= 10:
            nominator = i
            for k in range(1, i + 1):
                nominator += 1 / k
            denominator = 0
            for k in range(1, i + 1):
                denominator += 1 / k
            product *= nominator / math.sqrt(denominator)
            i += 1
        return product

    def _method_4() -> float:
        """while... while... loops"""
        product = 1
        i = 1
        while i <= 10:
            nominator = i
            k = 1
            while k <= i:
                nominator += 1 / k
                k += 1
            denominator = 0
            k = 1
            while k <= i:
                denominator += 1 / k
                k += 1
            product *= nominator / math.sqrt(denominator)
            i += 1
        return product

    print("for + for loops", _method_1())
    print("for + while loops", _method_2())
    print("while + for loops", _method_3())
    print("while + while loops", _method_4())


def task_7():
    print("Task 7: Infinite function and custom factorial")

    def _factorial(n: int) -> int:
        return 1 if n == 0 else n * _factorial(n - 1)

    eps = float(input("Enter accuracy: "))
    x = float(input("Enter x [-2 <= x <= 2]: "))

    if not (-2 < x < 2):
        print("x should be [-2 <= x <= 2].")
    else:
        k = 1
        term = ((-1) ** k * x ** (2 * k + 1)) / (k * _factorial(2 * k + 1))
        S = term
        while abs(term) > eps:
            k += 1
            term *= (-(x**2) * (k - 1)) / (k * (2 * k) * (2 * k + 1))
            S += term
        print(f"{S=} for {x=} over {k=} additions with {eps=}")


if __name__ == "__main__":
    print("My tasks number is 4!")
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()
