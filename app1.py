"""
    Napisz program, w którym z przykładowej listy liczb całkowitych
    wyznaczysz sumę tych liczb, które są podzielne przez podaną
    przez Ciebie wartość.
"""

def sum_numbers_divided_by(divisor: int, numbers: list[int]) -> int:
    if divisor == 0:
        raise ValueError('Cannot divide by zero!')
    return sum([n for n in numbers if n % divisor == 0])

def main() -> None:
    numbers = [32, 87, 12, 24, 25, 36]
    print(sum_numbers_divided_by(12, numbers))

if __name__ == '__main__':
    main()

