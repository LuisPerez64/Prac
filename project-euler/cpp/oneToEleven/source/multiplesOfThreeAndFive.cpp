#include <iostream>
#include <cstdlib>
#include <stdexcept>

int main(int argc, char* argv[]) {
  if  (argc != 2)
    throw 
      std::runtime_error("Not enough arguments to Command Line");

  int maxNum(atoi (argv[1])); /*Gets the total point to push in from cmdLine*/
  int total(0);

  for (int index = 1; index < maxNum; ++index)  
    if (index % 3 == 0 or index % 5 == 0)
      total += index;
  
  std::cout << "Total: " << total << std::endl << std::endl;

  return(0);
}    
