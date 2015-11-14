#include <iostream>
#include <map>
#include <string>

int main() {
  std::map <char, std::string> testMap;

  std::string testString;

  while (true) {
    std::getline(std::cin , testString);
    std::cout << testString;
  }

  return(0);
}
