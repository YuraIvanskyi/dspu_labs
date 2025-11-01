import math


def task_1():
    print("Task 1: Check point belongs to a given shaded area")
    print("My task: semicircle cut by x = y line at center")
    x, y = map(float, input("Enter x and y coordinates, separated by whitespace: ").split())
    print(f"Point ({x}, {y}) is in shaded area: {'Yes' if math.sqrt(x**2 + y**2) <= 1 and y <= x else 'No'}")


def task_2():
    print("Task 2: Function value for a value by interval")
    i = int(input("Enter iЄ[7,12]: "))
    a, b = 2.2, 0.3
    if 7 <= i <= 12:
        if i < 10:
            print(f"y = {a * i**4 + b *i}")
        elif i == 10:
            print(f"y = {math.tan(i + 0.5)}")
        else:
            print(f"y = {math.pow(math.e, 2 * i) + math.sqrt(a**2 + i**2)}")
    else:
        print("i out of the interval [7, 12]")


def task_3(number: int | str | None = None):
    print("Task 3: 4 digit number check")
    number = input("Enter a 4-digit number: ") if not number else str(number)
    print(f"{number} Has number 5: {'Yes' if '5' in number else 'No'}")
    print(f"{number} Has only even digits: {'Yes' if all(int(digit) % 2 == 0 for digit in number) else 'No'}")
    print(f"{number} Sum of digit greater than 10: {'Yes' if sum(int(digit) for digit in number) > 10 else 'No'}")
    first_two_digits = map(int, number[:2].split(""))
    last_two_digits = map(int, number[-2:].split(""))
    print(
        f"{number} First two digits sum less than last two: {'Yes' if sum(first_two_digits) < sum(last_two_digits) else 'No'}"
    )


def task_4():
    print("Task 4: Check triangle type")
    a, b, c = map(float, input("Enter sides of the triangle: ").split())
    if a + b <= c or a + c <= b or b + c <= a:
        print("Not a triangle")
    elif max(a, b, c) ** 2 > sorted([a, b, c])[0] ** 2 + sorted([a, b, c])[1] ** 2:
        print("Acute triangle")
    elif max(a, b, c) ** 2 < sorted([a, b, c])[0] ** 2 + sorted([a, b, c])[1] ** 2:
        print("Obtuse triangle")
    else:
        print("Right triangle")


def task_5():
    print("Task 5: Chessboard")
    col1, row1, col2, row2 = map(int, input("Enter coordinates of two cells on the chessboard: ").split())
    if not all(1 <= num <= 8 for num in [col1, col2, row1, row2]):
        print("Coordinates out of the chessboard range")
    print("YES") if col1 == col2 or row1 == row2 else print("NO")


def task_6():
    print("Task 6: Boxes")
    b1_length, b1_width, b1_height = map(float, input("Enter dimensions of box 1: ").split())
    b2_length, b2_width, b2_height = map(float, input("Enter dimensions of box 2: ").split())
    volume1 = b1_length * b1_width * b1_height
    volume2 = b2_length * b2_width * b2_height
    if volume1 > volume2:
        print("Box 2 can fit into box 1")
    elif volume1 < volume2:
        print("Box 1 can fit into box 2")
    else:
        print("Both boxes have the same volume")


def task_7():
    print("Task 7: Lines")
    a, b, c, d = map(float, input("Enter lengths of 4 lines: ").split())
    sorted_lines = sorted([a, b, c, d])
    print(
        "Rectangle possible"
        if sorted_lines[0] == sorted_lines[1] and sorted_lines[2] == sorted_lines[3]
        else "Rectangle impossible"
    )


def task_8():
    print("Task 8: 3 digit number to words")
    print("Could be done by string or numbers or whatever, I picked numbers")
    number = int(input("Enter a 3-digit number: "))
    words = {
        0: "нуль",
        1: "один",
        2: "два",
        3: "три",
        4: "чотири",
        5: "п'ять",
        6: "шість",
        7: "сім",
        8: "вісім",
        9: "дев'ять",
        10: "десять",
        11: "одинадцять",
        12: "дванадцять",
        13: "тринадцять",
        14: "чотирнадцять",
        15: "п'ятнадцять",
        16: "шістнадцять",
        17: "сімнадцять",
        18: "вісімнадцять",
        19: "дев'ятнадцять",
        20: "двадцять",
        30: "тридцять",
        40: "сорок",
        50: "п'ятдесят",
        60: "шістдесят",
        70: "сімдесят",
        80: "вісімдесят",
        90: "дев'яносто",
        100: "сто",
        200: "двісті",
        300: "триста",
        400: "чотриста",
        500: "п'ятсот",
        600: "шістсот",
        700: "сімсот",
        800: "вісімсот",
        900: "дев'ятсот",
    }
    result = []
    if number % 100 == 0:
        result.append(words[number])
    elif number % 10 == 0 or 0 < number % 100 < 20:
        result.append(words[(number // 100) * 100])
        result.append(words[number % 100])
    else:
        result.append(words[(number // 100) * 100])
        result.append(words[(number // 10 % 10) * 10])
        result.append(words[number % 10])
    print(" ".join(result))


if __name__ == "__main__":
    print("My tasks number is 4!")
    task_1()
    task_2()
    task_3(2624)
    # task_3("6614") # also works
    # task_3() # will ask for input
    task_4()
    task_5()
    task_6()
    task_7()
    task_8()
