#include "happyStrings.hpp"
#include <string>
#include <iostream>

int main(){
  std::cout << "Lets start the happy strings tester." <<std::endl;
  std::cout << "Input the string of letters to test:" <<std::endl;
  std::string happy;
  getline(std::cin, happy);
  
  std::cout << "What are the possible valid inputs to the string?:";
  std::string valid;
  getline(std::cin, valid);

  std::cout << "What is the letter that will be used to employ happiness?"
	    <<std::endl;
  char happyLetter;
  std::cin >> happyLetter;

  std::cout << "How many times does " << happyLetter << " have to pop up to "
	    <<std::endl << "make this string happy?: ";  
  int instances;
  std::cin >> instances;

  HappyString amIHappy(happy, valid, happyLetter, instances);
  //  HappyString test("ZXWWXY", "zxwy", 'w', 2);
  if(amIHappy.getResults())
    std::cout << "Seems that your string really is happy. Kind of creepily too"
	      <<std::endl;
  else
    std::cout << "Your string is sad, and you should feel sad."
	      <<std::endl;

  return 0;
}
