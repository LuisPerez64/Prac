/*
 * assertionIntro - Tests out the cassert library
 *
 * Author: Luis Perez
 *
 * Purpose: Basic program to test out the assert(--) function
 *
 * Usage: 
 *  Program is run, and fails on the first assertion point, because the index
 *  variable is greater than the upper limit(N_PRIMES) and the assertion fails
 *  and exits the program, somewhat dirtily, throw/catch may be better.
 */
#include <cassert>
#include <iostream>

const int N_PRIMES = 7;

int main(){

  int primes[N_PRIMES] ={2, 3, 5, 7, 11, 13, 17};

  int index = 10;

  //This assertion should, and does fail if index > N_PRIMES
  assert(index < N_PRIMES);
  assert(index >= 0); // Never gets here though, since above fails.
  std::cout << "The tenth prime is " << primes[index] << std::endl;

  return 0;
}
