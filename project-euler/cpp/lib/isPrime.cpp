#include <iostream>
#include <vector>

// Most efficient manner I have found, massvely cuts down time.
/*
  Is passed in a vector/array of all the primes that have been met so far.
  Takes those primes and mods the input number against the primes to that point
  ,applied an optimization technique, in whcih you only need to check to the
  square root of a number to know if it is prime. Explained in Sidenote
  If any number were to evenly divide this number before it got to its sqroot,
  then it is indeed not a prime, as it is divisible by a prime.
  SideNote::
   If there exists no number below x*x that would evenly divide a value then
   due to the principle that after the sqrt of a value, it's divisin pairs just
   flip, and repeat, if there exists none below the sqrt then there exists non 
   above it.
*/
bool isPrime(long int checkMe, std::vector<long int> Primes) {
  if (checkMe < 1) // No negative primes
    return false;

  std::vector<long int>::iterator primesIterator(Primes.begin());
  bool result(true); // The final return value.

  while (result) {
    if(primesIterator == (Primes.end() - 1) or *primesIterator > sqrt(checkMe))
      break; //Reaches and meets all needed points, isPrime.

    if(checkMe % (*primesIterator) == 0)  // The number is not prime if this
      result = false; // Makes result false, breaks out of the loop early

    ++primesIterator;// Move the iterator value forwards
  }

  return(result);
}
