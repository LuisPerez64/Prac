/*
 * AverageNNumbers --
 *  Takes input from the user in the form of an arbitrary number of numbers,
 *  and returns the average of those numbers back to the user.
 *
 * Author: Luis Perez
 * Purpose: Continued program spec development, and introductory 
 *    break/continue statements, with sentinel values.
 *
 * Usage:
 *  User inputs numbers until they feel that they are satisfied. Program 
 *  averages those numbers out, and prints out the average to the user.
 */

#include <iostream>
#include <iomanip>

void runAveragingProgram();

const int sentinelValue = -999; // Break away value for the averager...
int main() {
  runAveragingProgram();

  return(0);
}


void runAveragingProgram() {
  int inputCounter(1); // The number to divide by. 
  float inputNumber(0); // The number that is added to the sumtotal
  float inputNumbersTotal(0); // The running count.
  char answer('\0'); // answer used for toggle switchs.
  // Validates if user would like to output average at each entry
  bool toggle(false);
  
  std::cout << "Begin input of the numbers to be averaged." << std::endl 
	    << "When finished user input, input "<< sentinelValue 
	    << "." << std::endl;
  
  std::cout << "Would you like to know the average on every addition (y/n): ";
  std::cin >> answer;
  std::cout << std::fixed; // Fixed decimal notation throughout.

  if(answer == 'y' || answer == 'Y')
    toggle = true;
  
  // Used for the sake of using for loop.
  for(/*Blank*/;/*Blank*/;++inputCounter) {
    std::cout << "Input Number: ";  
    std::cin >> inputNumber;       
    
    if(inputNumber == sentinelValue)
      break;
   
    inputNumbersTotal += inputNumber;
    // Assures that there is not a FPE due to division by 0.
    if(toggle == true and inputCounter > 1)
      std::cout << std::setprecision(3) 
	<< "Average so far: " << (inputNumbersTotal / inputCounter)
	<< std::endl;
  }
  
  // Only printed out if at least one value is placed into the sum.
  if(inputCounter > 1)
    // Decrementing by one due to incrementation at last cycle in for loop.
    std::cout << std::setprecision(3) 
      << "Average of " << (inputCounter-1) << " input numbers is " 
      << (inputNumbersTotal / (inputCounter-1)) << "." << std::endl;
}
