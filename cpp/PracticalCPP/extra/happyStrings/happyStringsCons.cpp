#include "happyStrings.hpp"
#include <string>
#include <iostream>

HappyString::HappyString(std::string testString,std::string validValues,
			 char happyLetter,int instances){
  _testString = testString;
  _validValues = validValues;
  _happyLetter = happyLetter;
  _instancesNeeded = instances;
  convertToLower(_testString);
  convertToLower(_validValues);
}

bool HappyString::getResults() const{
  return amIHappy();
}

bool HappyString::amIHappy() const{
  if(_testString.length() < (unsigned int) _instancesNeeded)
    return false;

  bool result = false;
  int count = 0;

  for(unsigned int i = 0; i < _testString.length(); i++){
    if(_testString[i] == _happyLetter){
      count++;
      if(count == _instancesNeeded)
	result = true;
    }else
      count = 0;

    if(!validInput(_testString[i])){
      result = false;
      break;
    }
  }

  return result;
}

void HappyString::convertToLower(std::string &_string){

  for(unsigned int i = 0; i < _string.length(); i++)
    if(_string[i] >=65 && _string[i] <= 90)
      _string[i] += 32;
} 

bool HappyString::validInput(char check) const{
  for(unsigned int i = 0; i < _validValues.length(); i++)
    if(_validValues[i] == check)
      return true;

  return false;
}
