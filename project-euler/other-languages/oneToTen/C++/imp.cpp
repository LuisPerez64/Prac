#include <string>
#include <iostream>
#include <vector>

int main() {
  std::string link("123456789");
  std::vector<int> testVect;
  char inputMe;
  int product(1), newProduct(0);
  int count(0);
  int index(0);
  while (link.length() != 0) {
    inputMe =  link.at(0);
    testVect.push_back(inputMe - 48);
    link.erase(0, 1);
  }

  std::vector<int>::iterator testVectIt(testVect.begin());

  while (testVectIt != testVect.end()){
    
    while (count < 4){
      if (testVectIt == testVect.end())
	break;
      product *= *testVectIt; 
      ++testVectIt;
      ++count;
    }

    if (product > newProduct)
      newProduct = product;
    count = 0; product = 1;
    ++index;
    testVectIt = testVect.begin() + index;
  }
  std::cout << std::endl << newProduct << std::endl;

  return(0);
}
