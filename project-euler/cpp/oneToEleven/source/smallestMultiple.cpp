#include <iostream>

int bruteForceApproach (int , int);
int algorithmicApproach (int , int);

int main(int argc, char* argv[]) {
  int lowerBound, upperBound;
  int smallestMultiple;

  std::cout << "Lower & Upper Bounds: ";
  std::cin >> lowerBound >> upperBound;
  // Testing to se if I get the same answer both ways.
  smallestMultiple = (bruteForceApproach(lowerBound, upperBound));
  std::cout << "Smallest Multiple (bruteForce) is: " << smallestMultiple 
	    <<std::endl;

  smallestMultiple = (algorithmicApproach(lowerBound, upperBound));
  std::cout << "Smallest Multiple (algorithmic) is: " << smallestMultiple 
	    <<std::endl;

  return(0);
}
int bruteForceApproach (int lowerBound, int upperBound) {
  bool breakOut(false), checkMe(true);
  int answer(1);

  for (int index(upperBound) ; !breakOut ; index += upperBound) { 
    for (int temp(lowerBound); temp <= upperBound; ++temp)
      if (index % temp != 0)
	checkMe = false; // Prove that it's false
   
    if (checkMe){ // Found the value that satisfies all condiitons
      answer = index;
      breakOut = true; // Get out of it all
    }
    checkMe = true; // Reset thecheck value to true
  }

  return answer;
}

int algorithmicApproach (int lowerBound, int upperBound) {

  return 0;
}
