#include <iostream>
#include <cstdlib> // atoi

const double GOLDEN_RATIO(1.61803398875);

int main(int argc, char **argv) { 
  double calculateMyRatio, calculatedRatio;
  if (argc > 1) 
    calculateMyRatio = (atoi(argv[1]));
  else {
    std::cout << "Input number to be converted: ";
    std::cin >> calculateMyRatio;
  }
  calculatedRatio = calculateMyRatio * GOLDEN_RATIO;

  std::cout << "The golden number for this input is: " << calculatedRatio 
	    <<" ." << std::endl;

  return(0);
}
