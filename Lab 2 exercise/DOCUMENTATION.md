Lab 2 Documentation

Description of the test program :

test programm reads in an input file which is contains a set of inputs and outputs.
these will be used to compare each input with its corresponding output. the programme is
structured in such a way that it splits contents of the file to variables _input and _output.
from there we used a try catch (except Exception) so that it throws a "Tests failed" if the tests 
are not passed but "Tests passed" if every test was passed.
we implemented a unit tests which checks the function of primes bases on output.
a direct assert(PrimeNumbers(_input) == _output).
