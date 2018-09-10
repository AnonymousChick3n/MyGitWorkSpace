# Lab 2 Documentation
## purpose 
The purpose of this document is to show the analysis of a function that takes in a long positive integer number X and then it outputs the number of prime numbers less than or equal to X.It goes into detail and shows how we modified our input and it describes test program such as unit,integration and system testing.

## description of the code
We wrote a function of primes that accepts input and then return a list of primes,These prime numbers are then inserted in order in the
long integer array prime[]. If no prime numbers are possible error codes are returned in N. The use of the algorithm ”The sieve of Eratosthenes” to generate our primes.

What test cases do you envisage and how would you structure a testProg() to run and test all
your possible scenarios. The inputs for testing various conditions are to be read from some input
file .

## Modifications in the way parameters are passed
for the program to execte a list of primes our input must first be considered to be an integer type. We've
made the the program to stricly accept integer values, if some sort of input type is enterd then the program 
asks the user to enter the correct input type which is an  integer,since only intergers have prime values.if the user entered the correct input type then the program checks wherether the input is greater than 1 or not, if not an  empty list is returned or else the list with values corresponding to the list of primes.
 
## Description of the test program :
### test case unit testing
The unit test was implemented by having two test cases for the is_prime() module. The two test cases were test_primes() and test_non_primes().The test cases are implented using a class approach as compared to testProg(). 

#### test_primes() 
This test case reads in a standard text file (primes.txt) which contains a list of known prime numbers as a string. The test_primes() module reads the file as input then splits and maps the entries into an integer array called numbers.When test_primes iterates through the numbers array it is expected to pass.

#### test_non_primes() 
This test case reads in a standard text file (nonprimes.txt) which contains a list of known non prime numbers as a string. The test_non_primes() module reads the file as input then splits and maps the entries into an integer array called numbers.When test_non_primes iterates through the numbers array it is expected to pass.

 ### Intergration testing 
Integretion testing is meant to test the prime_numbers()
module which invokes is_prime().

#### test_primes_of_X()
This module reads in a text file named primes_of_X.txt which contains X and the first n primes before or including X. X is passed to the prime_numbers() module, where the prime_numbers() module returns a list of prime numbers before or including X and the result is compared to the first n primes before X which is read from the text file  primes_of_X.txt. This is done for multiple inputs. If the lists are equal then the test passed.


test programm reads in an input file which is contains a set of inputs and outputs.
these will be used to compare each input with its corresponding output. the programme is
structured in such a way that it splits contents of the file to variables _input and _output.
from there we used a try catch (except Exception) so that it throws a "Tests failed" if the tests 
are not passed but "Tests passed" if every test was passed.
we implemented a unit tests which checks the function of primes bases on output.
a direct assert(PrimeNumbers(_input) == _output) was is used to complete the test.


