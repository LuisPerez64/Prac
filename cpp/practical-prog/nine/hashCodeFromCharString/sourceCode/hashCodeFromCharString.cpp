/*
 * hashCodeFromString: 
 *  Takes in a string and produces a primitive hash code based on the chars
 *  in the given string.
 *
 * Author: Luis Perez
 *
 * Purpose: Continued functional programming. Continued string manipulation.
 *
 * Usgae: 
 *  User inputs a string to be converted into a basic hash code. The hash code 
 *  is formed by taking in the values of  each of the characters in the string
 *  and adding that integer value to a running total, returns that total to the
 *  caller.
 */

#include <iostream>
#include <string>

void runHashCodeFromCharString(void);
int hashCodeFromBasicString(std::string inputString);

int main() {
  runHashCodeFromCharString();
  return(0);
}

void runHashCodeFromCharString(void) {
  std::string inputString; // String to be turned into a hash code.
  int hashCodeTotal(0); // Total integer value of the input string. 
  
  std::cout << "Welcome to the hash code from basic strig function."
	    << std::endl;
  std::cout << "Please input the string to be converted: " << std::endl;
  std::getline(std::cin, inputString);
  
  hashCodeTotal = hashCodeFromBasicString(inputString);
  std::cout << "The total integer value of the iput string is: " 
	    << hashCodeTotal << std::endl;

  return;
}

int hashCodeFromBasicString(std::string inputString) {
  int totalHashCodeValue(0); // The vlaue of the string in hash code format.
  // Runs for the length of the input string. Adding the char values to total.
  for(unsigned int stringIndex(0);
      stringIndex < inputString.length(); ++stringIndex) 
    totalHashCodeValue += (short int) inputString.at(stringIndex);

  return(totalHashCodeValue);
}
