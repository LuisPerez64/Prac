/*
 * isPrime --
 *    the basic is prime function, checks if a number input by the user is a 
 *    prime number or not. Relays it to them.
 *
 * Author: Luis Perez
 * Purpose: First true algorithmic approach, pre proramming practice.
 *          Introductyion of the set object. 
 * Usage:
 *  Prompts user for a number
 *  Validates if the number that is input is prime
 *  Provides an appropriate response.
 */

#include <iostream>
#include <set>
#include "isPrime.hpp"
// variable that is used mainly to outline the fill point of the set initially
const int MAX_INPUT = 100;
void test();
int main() {

  runIsPrime();  
  return(0);
}

void runIsPrime(void) {
  std::set<int> setOfPrimes;
  int primeCheck(0);
  populateSet(setOfPrimes, 3, MAX_INPUT);
  std::cout << "Vector Size: " << setOfPrimes.size() << std::endl;

  do{
    std::cout << "Input number to validate if prime: ";
    std::cin >> primeCheck;
    if(primeCheck <= 0) {
      std::cout << primeCheck << " not Prime. No negative primes." <<std::endl;
      continue;
    }
   
    if(primeCheck <= MAX_INPUT) {
      lessThanMaxCheck(primeCheck, setOfPrimes);
      continue;
    }
    
    if(isPrimeAlg(primeCheck, setOfPrimes)) 
      std::cout << primeCheck << " Is a prime number." << std::endl;
    else 
      std::cout << primeCheck << " Is not a prime number." << std::endl;
    std::cout << "Vector Size: " << setOfPrimes.size() << std::endl;
   
  }while(runAgain());

  return;
}

    
bool isPrimeAlg(int checkMe, std::set<int> &setOfPrimes) {
  bool isPrime(false);
  if(traverseSet(checkMe, setOfPrimes)) {
    isPrime = true;
    setOfPrimes.insert(checkMe);
  }
  
  return(isPrime);
}

void lessThanMaxCheck(int primeCheck, std::set<int> &setOfPrimes) {
  if(setOfPrimes.find(primeCheck) == setOfPrimes.end())
    std::cout << primeCheck << " is not a prime number." << std::endl;
  else
    std::cout << primeCheck << " is a prime number." << std::endl;
}

bool traverseSet(int checkMe, std::set<int> &setOfPrimes) {
  std::set<int>::iterator primesIter(setOfPrimes.begin());  
  
  bool isPrime(true);

  for(/*Blank*/;(*primesIter * *primesIter) <= checkMe; ++primesIter) {
    if(checkMe % (*primesIter) == 0) {
      isPrime = false;
      break;
    }
    if(primesIter == setOfPrimes.end()) {// This is checking past the value
      // if needed. Populates up to the given index value.
      populateSet(setOfPrimes, *primesIter, checkMe);
      std::cout << *primesIter <<" here" <<  std::endl;
    }  
  std::cout << "Set Size: " << setOfPrimes.size() << std::endl;
  }
  return(isPrime);
}

void populateSet(std::set<int> &setOfPrimes, int iIndex, int jIndex) {
  setOfPrimes.insert(2);  
  if(iIndex % 2 == 0)
    ++iIndex; // To take into account even numbers being paced in.
  for(int index(iIndex); index <= jIndex; index += 2)
    if(isPrimeRaw(index))
      setOfPrimes.insert(index);
}

/** Tested already functions. Work as are needed. **/
bool isPrimeRaw(int checkMe) {  
  if(checkMe %2 == 0 || checkMe % 3 == 0)
    return(false); // If it's evenly divisible by 2 or 3 then not prime.

  bool isPrimeBool(true);
  for(int checkAgainst(3); checkAgainst < checkMe; checkAgainst += 2)
    if(checkMe % checkAgainst == 0) {
      isPrimeBool = false;
      break;
    }

  return(isPrimeBool);
}

bool runAgain() {
  bool runAgainBool(false);
  std::cout << "Would you like to check another number (y/n)?: ";
  char answer('\0');
  
  while((answer != 'y' and answer != 'Y') and 
	(answer != 'n' and answer != 'N')) {
    if(answer != '\0')
      std::cout << "Please input valid answer (y/n): ";
    std::cin >> answer;
  }
  
  if(answer == 'y' || answer == 'Y')
    runAgainBool = true;

  return(runAgainBool);
}
