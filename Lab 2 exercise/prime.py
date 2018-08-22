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

if __name__ == '__main__':

    max = input("Enter upper bound:")
    PrimeNumbers(max)
