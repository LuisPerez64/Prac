#include <iostream>
#include <cstdlib>
#include <stdexcept>
/*
 *Command line interaction to attain the needed upper limit.
 *Returns the sum of all the numbers below that limit, exclusive, that are 
 *even fibonacci numbers. Non recursive manner of doing the fibs calculation. 
 */
int main(int argc, char* argv[]) {
  if (argc != 2)
    throw 
      std::runtime_error("Need the number of the upper limit in cmdLine");

  int upperLimit(atoi(argv[1])); // make the string arg into an int
  int firstNum(1), secondNum(1), total(0);
  
  // The fibonacci sequence, (q = m +n / m = n, n = q) 'Looped'
  for (int result(secondNum);result < upperLimit;) {
    result = firstNum + secondNum;

    if ( result % 2 == 0)
      total += result;

    firstNum = secondNum;
    secondNum = result;
  }

  std::cout << "Total sum of the even Fibonacci values: " << total <<std::endl;
  return(0);
}
