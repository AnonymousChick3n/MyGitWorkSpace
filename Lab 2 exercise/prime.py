def prime_numbers(X):
    """Returns a list of the first n primes before and including X"""

    primes = []
    for number in range(2, X + 1):
        if is_prime(number):
            primes.append(number)
    return primes


def is_prime(number):
    """Returns true if number is a prime. Returns false otherwise"""
    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    if number < 2:
        return False

    return True






























def prime_numbers1(X):
    """primes"""

    X = 0
    numbers = []
    marked = [False] * X

    if(X < 2):
        print("No primes")
    elif (X == 2):
        numbers.append(2)
    else:
        numbers = range(X + 1)
        index = 2
        constant = numbers[index]
        variable = numbers[index]
        product = constant*variable

        while(constant * constant < X):

            if(product < X):
                marked[product] = True
                variable += 1
                product = constant*variable

            if(product >= X):
                for i in range(constant+1, X):
                    if(marked[i] == False):
                        constant = numbers[i]
                        break
                variable = constant
                product = constant*variable

        primes = []
        for i in range(2, len(marked)):
            if marked[i] == False:
                primes.append(numbers[i])
        X = len(primes)
        print("List of primes: ", primes)
        print("Number of primes: ", X)


def testProg():

    file = open("test.txt" , "r")

    n = 0

    for line in file:
        n += 1
        contents = line.split(":")
        _input = int(contents[0])
        _output =(contents[1].strip())
        try:
            assert(PrimeNumbers(_input) == _output)
            print("Test {0} passed".format(n))

        except Exception as e:
            print("Test {0} failed".format(n))


if __name__ == '__main__':
    X = int(input("Enter number: "))
    print(prime_numbers(X))

    '''invalid = True

    while (invalid):
        _max = input("Enter number: ")

        if (_max.isdigit()):
            invalid = False
        else:
            print("Integers only")

    testProg()


    #testProg()'''
