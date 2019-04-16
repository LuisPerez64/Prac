#include <iostream>

int sequenceSize(int testMe);

int main(int argc, char* argv[]) {
  int max(0);
  int sequenceSizeMe(0);
  int endPoint;

  std::cout << "What would the upper limit for the test be?: ";
  std::cin >> endPoint;

  std::cout << "Range is: " << sequenceSize(endPoint) << std::endl;
  
  for (int index(1); index < endPoint; ++index) 
    if ((sequenceSizeMe = sequenceSize(index)) > max)
      max = index;
  
  std::cout << "Max Sequence Size attained is: " << sequenceSizeMe
	    << ". From Index variable: " << max <<"." << std::endl <<std::endl;
 
  return(0);
}

int sequenceSize(int test) {
  int size(1);
  /*
    Collatz Conjecture:
    n -> n/2  if n is even
    n -> 3n+1 if n is odd
    Runs until N is == 1 
  */
  for (long int index(test); index != 1; ++size) 
    if (index % 2 == 0)
      index /= 2;
    else 
      index = (index * 3) + 1;

  return(size); // Inclusive of the first term of the sequence
}
  
