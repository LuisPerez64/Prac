/*
 * replaceDashWithUnderscore:
 *   Is given an input string. Takes that string, and if there are any dashes
 *   within it, replace them with an underscore.
 *
 * Author: Luis Perez
 * 
 * Purpose: Continued string manipulation. References work.
 *
 * Usage: 
 *  User inputs a string. If the string contains dashes, replace them, and
 *  present that to the caller. If not reflect that as well.
 */
#include <iostream>
#include <string>

void runReplaceDashWithUnderscore(void);
bool isChanged(std::string &inputString);

int main() {
  runReplaceDashWithUnderscore();
  return(0);
}

void runReplaceDashWithUnderscore(void) {
  std::string stringToValidate;
  std::cout << "Welcome to the dash replacement program." << std::endl;
  std::cout << "Please input the string to be evaluated: " << std::endl;
  std::getline(std::cin, stringToValidate);
  
  if(isChanged(stringToValidate))
    std::cout << "The string has been changed. Dashes have been replaced:"
	      << std::endl
	      << stringToValidate << std::endl;
  else
    std::cout << "The string has no dashes. It has not been changed." 
	      << std::endl;
  return;
}
bool isChanged(std::string &inputString) {
  bool isStringChanged(false); // Returned to user. Changes if dashes are found
  // Iterate through the given string.
  for(unsigned int stringIndex(0); stringIndex < inputString.length();
      ++stringIndex) 
    // If the string contains a dash, replace it with an underscore.
    if(inputString[stringIndex] == '-') {
      inputString[stringIndex] = '_';
      isStringChanged = true; // Change the returned value. Strings changed.
    }

  return(isStringChanged);
}
