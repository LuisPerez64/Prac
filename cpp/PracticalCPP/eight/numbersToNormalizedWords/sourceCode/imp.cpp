/*
 * Test Program to attain the needed inputs.
 */
#include <iostream>
#include <string>
int rangeFinder(int);
int main() {
  int input;
  while(true) {
    std::cin >> input;
    int temp(input % rangeFinder(input));
    //temp = input - temp;
    std::cout << temp << " " << rangeFinder(input) << std::endl;
  }

}

int rangeFinder(int input) {
  int returnValue(1);
  for(/* */; (returnValue *10) <= input; returnValue *= 10);
  
  return(returnValue);
}
