#include <iostream>
#include <cmath>
#include <vector>

inline void populateVector(std::vector<int> &inputVector, int upperBound);
void eliminateMe(int myPrime, std::vector<int> &inputVector, int);

int main() {
  std::vector<int> allNumbersBelowBound;
  int bound, index(1);
  std::cin >> bound;
  populateVector(allNumbersBelowBound, bound);
  
  std::vector<int>::iterator primesIter(allNumbersBelowBound.begin());
   
  return(0);
}


inline void populateVector(std::vector<int> &inputVector, int upperBound) {
  for(int lowerBound(2); lowerBound <= upperBound; ++lowerBound)
    inputVector.push_back(lowerBound);
}

void eliminateMe(int myPrime, std::vector<int> &inputVector) {
  
}
