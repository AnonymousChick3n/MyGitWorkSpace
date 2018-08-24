def PrimeNumbers(max):

    if(max > 1):
        primes = []
        for number in range(2, max+1):
            prime = True
            for divisor in range(2, number):
                if(number == 2):
                    prime = True
                elif(number%divisor == 0):
                    prime = False
            if(prime):
                primes.append(number)
        #print(primes)
        return str(primes)
    elif(max == 0 or max == 1):
        return str([])
    else:
        return str([])


def prime_numbers(max):

    N = 0
    numbers = []
    marked = [False]*max

    if(max < 2):
        print("No primes")
    elif (max == 2):
        numbers.append(2)
    else:
        numbers = range(max+1)
        index = 2
        constant = numbers[index]
        variable = numbers[index]
        product = constant*variable

        while(constant*constant < max):

            if(product < max):
                marked[product] = True
                variable += 1
                product = constant*variable

            if(product >= max):
                for i in range(constant+1, max):
                    if(marked[i] == False):
                        constant = numbers[i]
                        break
                variable = constant
                product = constant*variable

        primes = []
        for i in range(2, len(marked)):
            if marked[i] == False:
                primes.append(numbers[i])
        N = len(primes)
        print("List of primes: ", primes)
        print("Number of primes: ", N)

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

    invalid = True

    while (invalid):
        _max = input("Enter number: ")

        if (_max.isdigit()):
            invalid = False
        else:
            print("Integers only")

    testProg()


    #testProg()
