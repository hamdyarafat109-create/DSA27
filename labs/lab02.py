# -- decisions --------------------------------------------------------------

def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle sides")

    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"


def course_result(coursework, final, attendance):
    if not 0 <= coursework <= 40:
        raise ValueError("Invalid coursework mark")

    if not 0 <= final <= 60:
        raise ValueError("Invalid final mark")

    if not 0 <= attendance <= 100:
        raise ValueError("Invalid attendance")

    if attendance < 75:
        return "barred"
    elif final < 18:
        return "fail"
    elif coursework + final < 60:
        return "fail"
    else:
        return "pass"


# -- loops ------------------------------------------------------------------

def fizzbuzz(n):
    result = []

    for number in range(1, n + 1):
        if number % 3 == 0 and number % 5 == 0:
            result.append("FizzBuzz")
        elif number % 3 == 0:
            result.append("Fizz")
        elif number % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(number))

    return result


def is_prime(n):
    if n < 2:
        return False

    divisor = 2

    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1

    return True


def primes_below(n):
    result = []

    for number in range(2, n):
        if is_prime(number):
            result.append(number)

    return result


def first_repeated(values):
    seen = []

    for value in values:
        if value in seen:
            return value

        seen.append(value)

    return None


def count_pairs(n):
    return n * (n - 1) // 2


def calculator(command):
    parts = command.split()

    if not parts:
        raise ValueError("Empty command")

    operation, *arguments = parts

    try:
        match operation:
            case "add":
                if len(arguments) != 2:
                    raise ValueError("add requires two integers")

                a, b = map(int, arguments)
                return a + b

            case "mul":
                if len(arguments) != 2:
                    raise ValueError("mul requires two integers")

                a, b = map(int, arguments)
                return a * b

            case "neg":
                if len(arguments) != 1:
                    raise ValueError("neg requires one integer")

                return -int(arguments[0])

            case "sum":
                if len(arguments) < 1:
                    raise ValueError("sum requires at least one integer")

                return sum(map(int, arguments))

            case _:
                raise ValueError("Unknown command")

    except (TypeError, ValueError) as error:
        raise ValueError("Invalid command or arguments") from error


# -- functions --------------------------------------------------------------

def parse_int(text, default=None):
    try:
        return int(text)
    except (ValueError, TypeError):
        return default


def stats(*numbers):
    if not numbers:
        raise ValueError("At least one number is required")

    smallest = numbers[0]
    largest = numbers[0]
    total = 0

    for number in numbers:
        if number < smallest:
            smallest = number

        if number > largest:
            largest = number

        total += number

    mean = total / len(numbers)

    return smallest, largest, mean


def append_to(item, target=None):
    if target is None:
        target = []

    target.append(item)

    return target


def make_multiplier(k):
    def multiply(value):
        return value * k

    return multiply


def apply_n(f, x, n):
    result = x

    for _ in range(n):
        result = f(result)

    return result