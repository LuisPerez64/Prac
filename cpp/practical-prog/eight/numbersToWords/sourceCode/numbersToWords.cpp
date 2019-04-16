/*
 * numbersToWords --
 *   Is fed a number within the bounds of a long integer, and produces to the 
 *   user a phonetical version of each of the numbers that are being 
 *   represented.
 * 
 * Author: Luis Perez
 *
 * Purpose:
 *   Continued use of the new loop statements. 
 *
 * Usage: 
 *   User enters a number ie. 12345
 *   Console outputs "one two three four five"
 */

#include <iostream>
#include <string>

// Reproduces for the user a string form of the number that is input.
std::string makeOutputString(int inputVar);
/* Application program. Basic in and of itself. Calls the needed functions 
 * from here
 */
void runNumbersToWords();


int main() { 
  runNumbersToWords();
  return(0);
}


void runNumbersToWords(void) {
  int userInput(0); // The number that is to be converted to words
  std::string outputString; // Stirng that is to be output to the console 
  // String portion that is added in itself to the output string 
  std::string inputString;

  std::cout << "Please input the number to be printed out to the user: ";
  std::cin >> userInput;
  if(userInput == 0) { // Base case. Saves some lengthy booleans out.
    std::cout << "Zero" << std::endl;
    return; // Instant break.
  }
  /*
   * Runs until the input number is 0
   * Modifier: Divides the input number by 10 to make the number consistently
   *  modulo-able.
   */   
  for(/* Blank */ ; userInput > 0; userInput /= 10) {
    // Attain the string value for the number
    inputString = makeOutputString(userInput % 10);
    /*
     * Take the string and append it to the beginning of the output string.
     * This is to  take into account the fact that without it. The numbers 
     * would be inverted when they are output to the user.
     */
    outputString = inputString + " " + outputString;   
  }

  std::cout << "The numbers phonetically are: " << std::endl
	    << outputString << std::endl;
}
  
std::string makeOutputString(int inputVar) {
  std::string outputString; // Used to store the string that is returned.

  switch(inputVar) { // Switch acting on a moduloed 10 number will not exveed 9
  case 0:
    outputString = "zero";
    break;
  case 1:
    outputString = "one";
    break;
  case 2:
    outputString = "two";
    break;
  case 3:
    outputString = "three";
    break;
  case 4:
    outputString = "four";
    break;
  case 5:
    outputString = "five";
    break;
  case 6:
    outputString = "six";
    break;
  case 7:
    outputString = "seven";
    break;
  case 8:
    outputString = "eight";
    break;
  case 9:
    outputString = "nine";
    break;
  default:
    std::cout << "Test case. Should never be reached." << std::endl;
    break;
  }

  return(outputString);
}
