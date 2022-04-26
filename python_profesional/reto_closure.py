def make_divisors(n: int)-> int:
    def divisors(x: int)-> int:
        assert type(n)== int,  'only data type int can be used'
        assert n != 0, "You can't divide by zero"
        return f' {x/n} '
    return divisors

def run(): 
    division_by_3 = make_divisors(3)
    print(division_by_3(18))

    division_by_5 = make_divisors(5)
    print(division_by_5(100))

    division_by_18 = make_divisors(18)
    print(division_by_18(54))

if __name__ == '__main__':
    run()
