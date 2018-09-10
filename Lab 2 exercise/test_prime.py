import unittest
from prime import is_prime, prime_numbers

class TestPrime(unittest.TestCase):

    #unit test
    def test_primes(self):
        #open file for reading
        file = open("primes.txt", "r")
        line = file.readline()
        numbers = list(map(int, line.split()))

        for number in numbers:
            self.assertTrue(is_prime(number), msg="{} is not a prime.".format(number))
    #unit test
    def test_non_primes(self):
        #open file for reading
        file = open("nonprimes.txt", "r")
        line = file.readline()
        numbers = list(map(int, line.split()))

        for number in numbers:
            self.assertFalse(is_prime(number), msg="{} is a prime.".format(number))

    #integration test
    def test_primes_of_X(self):
        #open file for reading
        file = open("primes_of_X.txt", "r")
        for line in file:
            X = int(line)
            line = file.readline()
            primes = list(map(int, line.split()))
            self.assertEqual(prime_numbers(X), primes)
    #integration test
    def test_empty_set(self):
        #open file for reading
        file = open("empty_set.txt", "r")
        for line in file:
            X = int(line)
            line = file.readline()
            primes = list(map(int, line.split()))
            self.assertEqual(prime_numbers(X), primes)
            
if __name__ == '__main__':
    unittest.main()
