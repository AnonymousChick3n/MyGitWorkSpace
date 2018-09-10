# Lab 2 Documentation

## Modifications in the way parameters are passed
for thte program to execte a list of primes our input must first be considered to be an integer we've
made the the program to stricly accept integer values, if some sort of input type is enterd then the program 
asks the user to enter the correct input type which is an  integer.
if the user entered the correct input type then the program checks wherether the input is greater than 1 or not we
implementent such case to 
## Description of the test program :

test programm reads in an input file which is contains a set of inputs and outputs.
these will be used to compare each input with its corresponding output. the programme is
structured in such a way that it splits contents of the file to variables _input and _output.
from there we used a try catch (except Exception) so that it throws a "Tests failed" if the tests 
are not passed but "Tests passed" if every test was passed.
we implemented a unit tests which checks the function of primes bases on output.
a direct assert(PrimeNumbers(_input) == _output).


