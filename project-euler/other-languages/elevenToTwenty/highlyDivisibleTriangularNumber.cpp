#include <iostream>

int triangulate(int whichNumber); // Faster manner of attaining the Tri Number

// Returns to the user the amt of divisors to the given triangular number
int howManyDivisors(int triangularNum);

int main(int argc, char* argv[]) {
  int numOfDivisors(0); // This is the number of divisors to attain
  int triangularNum(0); // The resulting triangular number at index.
  // int trialNum(1); // Just a loop counter, external to be printable
  // Result of the total numbers that can divide index evenly
  int totalDivisors(0);
  
  std::cout << "How many divisors are you trying to attain?: ";
  std::cin >> numOfDivisors;  

  for (int trialNum(1); totalDivisors < numOfDivisors ; ++trialNum){
    triangularNum = triangulate(trialNum);
    totalDivisors = howManyDivisors(triangularNum);
  }

  std::cout << "The first number with at least " << numOfDivisors 
	    << " divisors is " << triangularNum << "." <<std::endl;

  return 0;
}

int triangulate(int whichNum) {
  return whichNum * (whichNum + 1) / 2; // The formula for the calculation
}

int howManyDivisors(int triangularNum) {
  int total(1);
  int divideByMe(1);

  while (divideByMe * divideByMe <= triangularNum) {
    if (triangularNum % divideByMe == 0)
      total+=2;

    ++divideByMe;
  }
  if(triangularNum == (divideByMe -1)*(divideByMe-1))
      total--;
  return (total);
}
