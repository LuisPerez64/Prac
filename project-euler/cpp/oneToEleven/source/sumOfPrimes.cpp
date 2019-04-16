/*
  Dependency: 
    isPrime.cpp Linked along with it

 */
#include <iostream>
#include <vector>

bool isPrime(long int checkMe, std::vector<long int> Primes);

int main(int argc, char * argv[]) {
  long int upperBound;
  long int prime(0);
  long int sumOfPrimes(2);
  std::vector <long int> Primes;
  std::cout << "What is the upper boundary of the prime to be checked?: ";
  std::cin >> upperBound;
  Primes.push_back(2);
  for (long int index(3);/*Empty on Purpose*/; index+=2)
    if (isPrime(index, Primes)){
      prime = index;
      if (prime >= upperBound) break;
      sumOfPrimes+= prime;
      Primes.push_back(prime);
    }

  std::cout << "The total of the primes below " << upperBound << " is: "
	    << sumOfPrimes << std::endl;

  return(0);
}
