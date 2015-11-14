#ifndef HAPPY_STR_H
#define HAPPY_STR_H

#include <string>

class HappyString{
public:
  HappyString(std::string testString, std::string validValues,
	      char happyLetter, int instancesNeeded);
  bool getResults() const;

private:
  std::string _testString;
  std::string _validValues;
  char _happyLetter;
  bool _result;
  int _instancesNeeded;
  void convertToLower(std::string &_string);
  bool validInput(char check) const;
  bool amIHappy() const;
};

#endif
