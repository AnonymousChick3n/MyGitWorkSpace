def PrimeNumbers(max):

    for number in range(2, max+1):

        prime = True
        for divisor in range(2, number):

            if(number == 2):
                prime = True
            elif(number%divisor == 0):
                prime = False

        if(prime):
            print(number)

def prime_numbers(max):

    N = 0
    numbers = []
    marked = [False]*max
    print(len(marked))
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

        print(primes)
if __name__ == '__main__':

    max = input("Enter upper bound:")
    #PrimeNumbers(max)

    prime_numbers(max)

