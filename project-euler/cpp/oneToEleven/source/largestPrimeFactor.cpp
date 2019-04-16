// Copyright Luis Perez 2015
// Brute force method for finding the largest Prime Factor of a given number
// Could be streamlined a lot better, but I don't as of yet know how to.
// Rewriting this as well to make the main point I want of Modularity.

#include <iostream>
#include <vector>
#include <cmath>
bool isPrime(long int checkMe, std::vector<int> primesList);

int main(int argc, char* argv[]) {  
  long int inputNumber;
  int max(1), testNumber;

  // Try and make it a stand point, make a container ~> make an iterator.
  std::vector<int> Primes;
  std::vector<int>::iterator primesIterator(Primes.begin());
 
  std::cout << "What number would you like to test out: ";
  std::cin >> inputNumber;
  if (inputNumber >= 99999) // After this point things are a bit shaky. 
    testNumber = sqrt(inputNumber); // Find its sqrRoot and use as input.
  else 
    testNumber = inputNumber; 

  // Store the Primes that fit under the square root of the given number
  Primes.push_back(2);
  for(int index = 3; index <= testNumber; index+= 2)
    if (isPrime(index, Primes))
      Primes.push_back(index);

  // Check the list of primes from the end to the beinning, if value is prime 
  // then the max remains at 1.
  for (primesIterator = Primes.end() - 1; // Primes.end() == 0
       primesIterator != Primes.begin(); // Go until the last prime is found
       --primesIterator)
    if (inputNumber % (*primesIterator) == 0) {
      max = *primesIterator; // It fits the bill, go forth and print it
      break;
    }
  
  std::cout << "Highest Prime Factor: " << max << std::endl << std::endl;
 
  return(0);
}

bool isPrime(long int checkMe, std::vector<int> listOfPrimes) {
  if (checkMe < 1) // No negative primes
    return false;
  std::vector<int>::iterator primesIter(listOfPrimes.begin());
  bool result(true); // The final return value.
  
  while (result and primesIter != listOfPrimes.end()) {
    if ((*primesIter)*(*primesIter) > checkMe) 
      break;

    if(checkMe % (*primesIter) == 0){// The number is not prime if this is met
      result = false; // Makes result false, breaks out of the loop early
      break;
    }
    ++primesIter; // Decrement the index value to be used in the above equation
  }

  return result;
}
