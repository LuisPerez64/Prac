#ifndef IS_PRIME_HPP
#define IS_PRIME_HPP

void runIsPrime(void);

/*
 * Fills in the primes below the endIndex to be used in the given operations.  
 * uses the basic isPrimeRaw function to do this, only time this function is 
 * used, and this function is also run prior to any other operations.
 * Changed this function. Added values for index to make it malleable, and 
 * useable at any point in the program.
 */
void populateSet(std::set<int> &setOfPrimes, int firstIndex, int endIndex);

/*                                                                             
 * Basic prime function, fast enough when numbers are below 10k used to        
 * populate the set initially. Used in populate set function.                  
 */
bool isPrimeRaw(int checkMe);

/*
 * Fills a set, with the populate set function.
 * Runs traversal through the set attempting to find out if the number is 
 * divisible by any prime before its square root, if not then the number itself * is prime.
 * Add that number to the primes list.
 */
bool isPrimeAlg(int checkMe, std::set<int> &setOfPrimes);

/*
 * Basic set traversal. runs trhrough the set moduloing until it reaches the 
 * needed break point.
 */
bool traverseSet(int checkMe, std::set<int> &setOfPrimes);

/*
 * This is run on any number below the limit, and just does a set find run
 * through instead of checking against all numbers leading up to the one in
 * question.
 */
void lessThanMaxCheck(int primeCheck, std::set<int> &setOfPrimes);

/*
 * Basic bool, asks if the user would like to run the program again.
 */
bool runAgain();


#endif  // IS_PRIME_HPP
