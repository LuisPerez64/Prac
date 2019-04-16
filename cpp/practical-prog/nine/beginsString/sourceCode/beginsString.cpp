/*
 * beginsString:
 *   Takes in two strings, if the first string begins the second string, then
 *   returns true.
 *
 * Author: Luis Perez
 *
 * Purpose: String Manipulation. Functional Programming Practice. 
 *
 * Usage:
 *  User inputs two strings, function returns a bool, and proceeds based on 
 *  that.
 */

#include <iostream>
#include <string>

void runBeginsString(void);
bool beginsString(const std::string &stringOne, const std::string &stringTwo);
// Basic overload of the == function for strings. Yes it's written but so what.
inline bool operator==(const std::string leftHandString, 
		       const std::string rightHandString);

int main() {
  runBeginsString();
  return(0);
}

void runBeginsString(void) {
  // Strings that are supplied by the user to test the function.
  std::string inputStringOne;
  std::string inputStringTwo;
  
  std::cout
    << "Welcome to the begins string program." << std::endl;
  
  // Get the users input.
  std::cout << "Input the first string: " << std::endl;
  std::getline(std::cin , inputStringOne);
  std::cout << "Input the second string: " << std::endl;
  std::getline(std::cin , inputStringTwo);

  // Heart of the program, calls the function to verfy the strings contents.
  if(beginsString(inputStringOne, inputStringTwo))
    std::cout << "Input string one, begins input string two." 
	      << std::endl;
  else
    std::cout << "Input string one, does not begin input string two." 
	      << std::endl;
  
  return;
}

bool beginsString(const std::string &stringOne, const std::string &stringTwo) {
  // Base case first string is longer than the second, can't begin it.
  if(stringOne.length() > stringTwo.length())
    return false;
  
  bool returnValue(false);
  
  std::string tempString(stringTwo.substr(0, stringOne.length()));
  if(tempString == stringOne)
    returnValue = true;
  
  return(returnValue);
}
 
inline bool operator==(const std::string leftHandString, 
		       const std::string rightHandString) {
  // If they are not the same length then they can't be equal.
  if(leftHandString.length() != rightHandString.length())
    return false;
  
  bool isMatch(true); // Is it a match?
  // Iterate through both the strings. Checking match at every intersection.
  for(unsigned int stringIndex(0); stringIndex < leftHandString.length();
      ++stringIndex)
    if(leftHandString[stringIndex] != rightHandString[stringIndex]) {
      isMatch = false; // If they ever don't match break, return false.
      break;
    }
  
  return(isMatch); // Is it a match?
}
