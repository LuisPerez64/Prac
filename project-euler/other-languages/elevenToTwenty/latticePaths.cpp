#include <iostream>

#define ULLI unsigned long long int
 
ULLI factorial(int factorMe);
ULLI choose(int input, int chooseHowMany);
void test(void);

int main(int argc, char *argv[]) { 
  ULLI latticePathLength(0);
  int matrixXVertex(0), matrixYVertex(0); // Hold the dimensions of the matrix.
  int inputTotal(0); // Holds the number to be sent to choose;
  test();
  std::cout << "Please input the size of the matrix to be traversed: "
	    << std::endl << "X Axis: ";
  std::cin >> matrixXVertex;
  std::cout << "Y Axis: ";
  std::cin >> matrixYVertex;

 
  inputTotal = matrixYVertex + matrixXVertex;
  latticePathLength = choose(inputTotal, matrixXVertex);

  std::cout 
    << std::endl
    << "For a matrix of size " << matrixXVertex << "x" << matrixYVertex
    << std::endl << "The total lattice path would be: " 
    << latticePathLength <<"." << std::endl; 
  
  return(0);
}

ULLI factorial (int factorMe) {
  ULLI result(1);
  while (factorMe - 1) { // Smart Way of getting while true...
    result*= factorMe;
    --factorMe;
  }

  return(result);
}

ULLI choose(int input, int chooseHowMany) {
  ULLI topHalf(factorial(input));
  ULLI bottomHalf
    (factorial(chooseHowMany) * factorial(input - chooseHowMany));
  ULLI combinations
    (topHalf / bottomHalf);

  return(combinations);
}

void test(void) {
  int input;
  std::cin >> input;

  ULLI result(factorial(input));
  std::cout << result;
}
