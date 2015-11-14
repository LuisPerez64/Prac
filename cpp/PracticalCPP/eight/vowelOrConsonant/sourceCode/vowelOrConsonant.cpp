/*
 * vowelOrConsonant--
 *   Program takes in a character or string from user, tells user if the given
 *   character at the indexed point of the string is a vowel.
 *
 * Author: Luis Perez
 *
 * Purpose: Continued use of more advanced conditional statements.
 *
 * Usage: User inputs a stirng or a character. Is supplied with whether 
 *        specified letter at index, or letter is a vowel.
 */
#include <iostream> // std::cin | std::cout 
// std::string | std::getline(inputSource, inputInto) | erase(begin, end)
#include <string>
#include <algorithm> // std::remove(begin, end, char)


void runIsVowel(void);
bool isVowel(char testInput);

int main(void) {
  runIsVowel();
}    
void runIsVowel(void) {
  std::string inputString;
  
  std::cout << "Input the letters or word that you would like to check: ";
  std::getline(std::cin , inputString);
  // erases any spaces, not so much all other characters
  inputString.erase
    (std::remove(inputString.begin(), inputString.end(), ' '), 
     inputString.end());
  // Used a for loop for the sake of the advanced loop statements.
  for(/* */;inputString.length() > 0; inputString.erase(0, 1))
    if(isVowel(inputString.at(0)))
      std::cout << inputString.at(0) << " is a vowel." << std::endl;
    else 
      std::cout << inputString.at(0) << " is not a vowel." << std::endl;
   
}

bool isVowel(char testInput) {
  // Switch would be highly inefficient for this....
  bool result(false);
  if(testInput == 'a' || testInput == 'A' or
     testInput == 'e' || testInput == 'E' or
     testInput == 'i' || testInput == 'I' or 
     testInput == 'o' || testInput == 'O' or
     testInput == 'u' || testInput == 'U')
    result = true;

  return(result);
}
