# Lab 2 Documentation
## purpose 
The purpose of this document is to show the analysis of the function that takes in a positive long integer number X and outputs  the number of prime numbers less than or equal to X. Showing how we modified our input and the description of the test program.

## description of the code
These prime numbers are then inserted in order in the
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

test programm reads in an input file which is contains a set of inputs and outputs.
these will be used to compare each input with its corresponding output. the programme is
structured in such a way that it splits contents of the file to variables _input and _output.
from there we used a try catch (except Exception) so that it throws a "Tests failed" if the tests 
are not passed but "Tests passed" if every test was passed.
we implemented a unit tests which checks the function of primes bases on output.
a direct assert(PrimeNumbers(_input) == _output) was is used to complete the test.


