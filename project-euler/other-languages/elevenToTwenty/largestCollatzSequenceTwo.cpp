#include <iostream>

int collatzSequence(int input);

int main(int argc, char *argv[]) {
  int maxSequenceSize(0), sequenceSize(0), benchMark, indexExtern(0);
  std::cout << "What is the benchmark for this, end point: ";
  std::cin >> benchMark;
  
  for (int index(benchMark - 1); index >= 2; --index) {
    sequenceSize = collatzSequence(index);
   
    if (sequenceSize > maxSequenceSize){
      maxSequenceSize = sequenceSize;
      indexExtern = index;
    }
  }
 
  std::cout << "Max sequence size: " <<  maxSequenceSize << std::endl
	    << "From index point: " << indexExtern << std::endl;
  return(0);

}

int collatzSequence(int index) {
  int size(1);
  for (long int num(index); num != 1; ++size)    
    if (num % 2 == 0)
      num/=2;
    else 
      num = (3 * num) + 1;

  return(size);
}
