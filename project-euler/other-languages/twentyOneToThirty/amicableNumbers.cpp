#include <iostream>
#include <vector>
#include <algorithm>

int sumOfDivisors(int);
bool isAmicable (int, int);

int main(int argc, char *argv[]) {
  std::vector<int> amicableNumbers;
  std::vector<int>::iterator amicableIter;
  int amicableNumbersTotal(0), benchMark(0);
  std::cout << "Input end point for the amicable number check: ";
  std::cin >> benchMark;


  for (int firstCheck(1); firstCheck <= benchMark; ++firstCheck) {
    int secondCheck(sumOfDivisors(firstCheck));
    if (firstCheck != secondCheck)
      // Can divide by two at the end, to invalidate duplicates, to make this
      // a bit faster, but doing this the hard way instead
      // Guarantees no duplicates in the computation.
      if (find (amicableNumbers.begin(), amicableNumbers.end(), firstCheck) ==
	  amicableNumbers.end())
	if (find (amicableNumbers.begin(), amicableNumbers.end(), secondCheck) 
	    == amicableNumbers.end())
	  if (isAmicable(firstCheck, secondCheck)){
	    amicableNumbers.push_back(firstCheck);
	    amicableNumbers.push_back(secondCheck);
	  }
  }
  
  for (amicableIter = amicableNumbers.begin();
       amicableIter != (amicableNumbers.end());
       ++amicableIter)
     amicableNumbersTotal += *amicableIter;

  std::cout << "The total of all the amicable numbers to this point is: "
	    << amicableNumbersTotal << "." << std::endl;
 
  return(0);
}

int sumOfDivisors(int input) {
  int divisors(input / 2);
  int total(0);

  while (true) {
    if ( divisors == 0)
      break;

    if ((input % divisors) == 0)
      total += divisors;
    --divisors;
  }

  return total;
}

bool isAmicable(int inputOne, int inputTwo) {
  int temp(sumOfDivisors(inputTwo));
  bool result(false);

  if (temp == inputOne)
    result = true;

  return(result);
}
