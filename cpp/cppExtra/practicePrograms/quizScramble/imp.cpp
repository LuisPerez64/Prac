#include <vector>
#include <string>
#include <iostream>

int main() {
  std::vector<std::string> input;
  std::vector<std::string>::iterator it(input.begin());
  for (int inputOne(0); inputOne < 5; inputOne++)
    input.push_back("lookiksfaf");
  
  while (it != input.end()) {
    std::cout << input.at(1) << std::endl;
    ++it;
  }
  return 0;
}
