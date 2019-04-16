#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <stdexcept>

long unsigned int getMax(int traverseLength, std::vector<int> inputMatrix);
void fillMatrix(std::vector<int> &inputMatrix);
int traverseMatrix(std::vector<int> inputMatrix,
		   int traverseLength);

int main(int argc, char *argv[]) {
  if (argc != 2)
    throw 
      std::runtime_error("Please input the points for traversal length");

  std::vector<std::vector<int> > matrixOfInts;
  int traverseLength(atoi(argv[1]));

  fillMatrix(matrixOfInts);
  long unsigned int result(traverseMatrix(matrixOfInts, traverseLength));

  std::cout << "The biggest product going through this matrix with the given" 
	    << std::endl << "traversal length of " << traverseLength << " "
	    << "is: " << result << std::endl << std::endl;  
    
  return(0);
}

// Will do this again with the filestream points, and read from a file instead.
// This works but is somewhat inefficient manner of doing all this.
void fillMatrix(std::vector<int> &inputMatrix) {
  std::string inputString;
  char unconvertedChar;

  while (std::cin) { // Until the end of the file is met, 
    std::vector<int> vectorOfValues;
    std::getline(std::cin , inputString);
  
    for ( ;inputString.length() != 0; ) { // Runs until the inputString's blank
      unconvertedChar = inputString.at(0); // Stores the first char 
      vectorOfValues.push_back(unconvertedChar - 48); // makes the char a num
      inputString.erase(0 , 1); // Erases the first variable from the string.
    }

    inputMatrix.push_back(vectorOfValues); // Bring the vector into the matrix
  }
  return; 
}
//Reason this didn't work was that I wasn't treating the whole input like one
// number, but as rows of numbers, which is wrong...
int traverseMatrix(std::vector<std::vector<int> > inputMatrix,
		   int traverseLength) {
  long unsigned int maxProduct(0);
  long unsigned int product(0);
 
  for (int iIndex(0); (unsigned)iIndex < inputMatrix.size(); ++iIndex){
    product = getMax (traverseLength, inputMatrix.at(iIndex));
    if (product > maxProduct)
	maxProduct = product;
  }

  return(maxProduct);
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
  
