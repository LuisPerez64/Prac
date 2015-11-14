/*
 * calc -- A four function calculator
 * 
 * Author: Luis Perez
 *
 * Purpose: Takes input from the user, and relays calculations back to them
 *           the results of said calculation.
 *
 * Usage: Input operator and the number to change the calculation by
 *        Valid operators are (+,-,*,/)
 *        ex. Result: 0
 *            Enter Operator and Number:+ 100
 *            Result: 100
 *            Enter Operator and Number:
 */

#include <iostream>

void calculator(void);

int main(int argc, char* argv[]) {
  calculator(); // No setup is needed 
  return(0);
}

void calculator(void) {
  int result(0);  // The result displayed to the user
  char calcOperator('\0');  // The operator (+-*/) modifying results value
  int numberActingOnResult(0); // The number that is modifying results value

  while(true) { 
    std::cout << "Result: " << result << std::endl;
    
    std::cout << "Enter operator and number: ";
    std::cin >> calcOperator; // Broke them apart to reduce annoyance to user.
    if(calcOperator == 'q' || calcOperator == 'Q') // Can't act within switch
      break;
    std::cin >> numberActingOnResult; // Only runs if not quitting.

    switch(calcOperator) {
    case '+':
      result += numberActingOnResult;
      break;
    case '-':
      result -= numberActingOnResult;
      break;
    case '*':
      result *= numberActingOnResult;
      break;
    case '/':
      if (numberActingOnResult == 0) {
	std::cout << "Cannot divide by 0. Operation negated." << std::endl;
	continue; // The continue goes back to top of while loop.
      }
      result /= numberActingOnResult;
      break;
    default:
      std::cout << "Unknown Operator '" << calcOperator <<"'."<< std::endl;
      break;
    }

  }
}
