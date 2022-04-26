def odd_number(number: int) -> bool:
    """Returns True if number is odd or False if the number is not odd"""
    results_list = [x for x in range(1, number) if number % 2 == 0]
    return len(results_list) == 0

def run():
    number: int = 6
    number_is_odd: bool = odd_number(number)
    print(f'Is {number} a odd number? {number_is_odd}')


if __name__ == '__main__':
    run()