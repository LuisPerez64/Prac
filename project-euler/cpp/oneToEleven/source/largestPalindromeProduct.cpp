#include <iostream>
#include <string>
#include <sstream>

bool isPalindrome (std::string checkMe);
std::string convertedInt(int x);

int main(int argc, char * argv[]) {
  int product(0); // Tested string once converted
  int upperLimit(0), lowerLimit(0); // Limits of the function
  int maxPalindrome(0); // Holds the biggest palindrome found
  int iIndexPos(0), jIndexPos(0); // To find out the product taht causes it.

  std::cout << "Lower and Upper Limit?: ";
  std::cin >> lowerLimit >> upperLimit;

  for (int iIndex(lowerLimit); iIndex <= upperLimit; iIndex++)
    for (int jIndex(lowerLimit); jIndex <= upperLimit; jIndex++){
      product = iIndex * jIndex;
   
      if (isPalindrome(convertedInt(product)))
	if (product > maxPalindrome){
	  maxPalindrome = product;
	  iIndexPos = iIndex;
	  jIndexPos = jIndex;
	}
    }
 
  std::cout << "Max palindrome is: " << maxPalindrome << " attained from "
  << iIndexPos << " x " << jIndexPos << "." << std::endl << std::endl;
}

bool isPalindrome (std::string checkMe){
  bool result(true);
  while (checkMe.length() > 1 and result == true){
    /*
      If the first value in the string is not equal to the last value of the 
      string, then the input string is not a palindrome. Comments are important
      even on the basic points...
     */
    if (checkMe.substr(0 , 1) != 
	checkMe.substr(checkMe.length() -1, std::string::npos))
      result = false;
    // Get the substr for the middle portion of the string in, works great.
    // Don't know why i needed length -2 instead of length -1  
    checkMe = checkMe.substr(1, checkMe.length() - 2);
 }    
  return(result);
}
/*
  Pre: Is given an integer
  Post: Converts that integer in a string object
  
  @Params: integer input
  @Returns: String version of the integer that was input.
  
  @Function:
    Instantiates a stringStream, within which to store the converted value
    uses that stream within a while loop,
    Gets the last value of the integer by modulo division, appending it to the 
    string current, since this is a check for palindrome-ness?, the only thing
    that matters is that the string be the same both ways, so this method works
    The number is however input backwards...
    After the curent point is added, go to the next value b dividing the int
    by 10, yielding a clean ints floor, does this until the result of that is 
    0, beaks and returns the needed string.
 */
std::string convertedInt(int input) {
  std::stringstream outputSS;

  while (input != 0){    
    outputSS << input % 10; // Pushes them all back in converting them to chars
    input /= 10; // Decrements the index to get the next variable
  }

  return(outputSS.str());
}
