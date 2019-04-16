#include <iostream>
#include <vector>
#include <cstdlib>
#include <stdexcept>
#include <string>

void fillVector(std::vector<int> &series);
long unsigned int getMax(int, std::vector<int> series);

int main(int argc ,char * argv[]) {
  if (argc != 2)
    throw 
      std::runtime_error ("Please input traversal length into cmd line");

  std::vector <int> seriesOfNumbers;
  int traverseLength(atoi(argv[1]));

  fillVector(seriesOfNumbers);
  long unsigned int result(getMax(traverseLength, seriesOfNumbers));

  std::cout << "The biggest product going through this matrix with the given"
            << std::endl << "traversal length of " << traverseLength << " "
            << "is: " << result << std::endl << std::endl;

  return(0);
}  
  
void fillVector(std::vector<int> &series){
  std::string inputString;
  char unconvertedChar;
  
  while (std::cin) {
    std::getline(std::cin, inputString);
    
    while (inputString.length() != 0) {
      unconvertedChar = inputString.at(0);
      series.push_back(unconvertedChar - 48);
      inputString.erase(0, 1);
    }
  }

  return;
}

long unsigned int getMax(int traverseLength, std::vector<int> inputMatrix) {
  long unsigned int total(1);
  long unsigned int newTotal(0);
  int multIndex(0);
  int count(0);
  std::vector<int>::iterator it(inputMatrix.begin());

  while (it != inputMatrix.end()) {
    while (count < traverseLength){
      if (it == inputMatrix.end())
        break;
      total *= *it;
      ++it;
      ++count;
    }

    if (total > newTotal)
      newTotal = total;
    // Update everything here, to make things work forward                      
    count = 0;
    total = 1;
    ++multIndex;
    it = inputMatrix.begin() + multIndex;
  }

  return newTotal;
}

