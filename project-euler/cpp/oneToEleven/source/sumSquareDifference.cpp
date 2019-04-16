#include <iostream>
/*
  Purpose: Find the difference between the square of a given group of sums, and
  the sum of the square of the given group...
 */
int main() {
  std::cout << "Input the upper bound of the calculation: ";
  int upperBound;
  std::cin >> upperBound;
  int sumOfSquares(0), squareOfSums(0);
  
  for(int i(1); i <= upperBound; ++i){
    sumOfSquares += i*i;
    squareOfSums += i;
  } squareOfSums *= squareOfSums;

  std::cout << "The square sum difference of these values is: "
	    << squareOfSums - sumOfSquares << std::endl;

  return(0);
}
