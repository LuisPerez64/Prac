#include <iostream>
#include <vector>

bool isPrime(int checkMe, std::vector<int> primesIndex);

int main(int argc, char* argv[]) { 
  unsigned int indexInput; 
  std::vector<int> Primes;  //For every Container, an iterator.
  std::vector<int>::iterator primesIterator;
  
  std::cout << "Which Prime would you like to attain?: ";
  std::cin >> indexInput;
  Primes.push_back(2); // Insert the first prime/ reduce time exponentially.
  //Decrement index y the elt that has been passed in. 
  for(int index = 3; Primes.size() < indexInput; index += 2)
    if (isPrime(index, Primes))
      Primes.push_back(index);
    
  //Iterators last indexed point is always null
  std::cout << "The "<< indexInput << "'th prime is: " << *(Primes.end() - 1)
	    << std::endl << std::endl;
  
  return(0);
}

bool isPrime(int checkMe, std::vector<int> listOfPrimes) {
  if (checkMe < 1) // No negative primes
    return false;
  std::vector<int>::iterator primesIter(listOfPrimes.begin());
  bool result(false);

  //Runs until the end of the primes is met technically never getting here
  while (primesIter != listOfPrimes.end()) {
    /*
      The squre of a nmber is the last point at which unique pairs of divisors
      can be found, if there exists none below the square, there exists none
      above it that can divide it. Is Prime
    */
    if ((*primesIter) * (*primesIter) > checkMe){
      result = true;
      break; 
    }	
    if(checkMe % *primesIter == 0){  // The number is not prime if this is met
      result = false; // Makes result false, breaks out of the loop early
      break;
    }
    ++primesIter;
  }
  
  return(result);
}
