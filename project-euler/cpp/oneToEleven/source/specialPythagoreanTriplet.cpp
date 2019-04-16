#include <iostream>
#include <cmath>
#include <cstdlib>

int main(int argc, char* argv[]) {
  int varA(3), varB(4), varC(5);
  int benchMark(1000);
  int tempA(varA+1), tempB(varB+1), tempC(varC+1);
  
  std::cout << "Input the upper limit of the calculations: ";
  std::cin >> benchMark;

  while (true) {
    if (pow (varA, 2) + pow (varB , 2) == pow (varC, 2))
      if (varA + varB + varC == benchMark)
	break;
    
    varC++;
    if (varC == benchMark) {
      varB++;
      varC = varB + 1;
    }

    if (varB == benchMark/2) { // resets everything to a basic form
      varA = tempA;
      varB = tempB;
      varC = tempC;
      ++tempA; // Make sure that everything follows a < b < c format.
      ++tempB;
      ++tempC;
    }
      
    if (varA >(benchMark/3)) { // BasicError check, should A exceed half of the
      // Benchmark, the benchmark is not a proper summationable sequence.
      std::cout << "ERROR: " << benchMark 
		<< " This number is not summable into." << std::endl;
      exit(2);
    }
    
  }

  std::cout << varA << " " << varB << " " << varC << std::endl;
  std::cout << varA*varB*varC << std::endl;

  return(0);
}
