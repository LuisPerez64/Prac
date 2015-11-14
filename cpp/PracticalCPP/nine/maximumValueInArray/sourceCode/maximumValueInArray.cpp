/*
 * maximumValueInArray:  
 *  Function is given an array, and returns to the caller the largest value
 *  that is found in the array.
 *
 * Author: Luis Perez
 *
 * Purpose: Array manipulation. Functional programming basics.
 *
 * Usage: 
 *   User inputs numbers to be stored in an array. After the fact the largest 
 *   number in that array is then returned to them.
 */
#include <iostream>

void runMaximumValueInArray(void);
int& findMaximumValue(int array[], int arrayLength);

const int ARRAY_LENGTH = 10;
int main() {
  runMaximumValueInArray();
  return(0);
}


void runMaximumValueInArray(void) {
  int arrayOfInts[ARRAY_LENGTH];
  int inputNumberForArray(0); // Number to be placed in array.
  std::cout << "Welcome to the array largest value finder." << std::endl;
  std::cout << "Please begin inputting numbers into the array." << std::endl;
  
  for(int inputIndex(0);inputIndex<ARRAY_LENGTH;++inputIndex) {
    std::cout <<"Number to input: ";
    std::cin >> inputNumberForArray;
    arrayOfInts[inputIndex] = inputNumberForArray;
  }
  int& largestValue(findMaximumValue(arrayOfInts, ARRAY_LENGTH));

  std::cout << largestValue 
	    << " is the largest input value in the given array." << std::endl;
}
int& findMaximumValue(int array[], int arrayLength) {
  int arrayIndex(0);
  for(int checkAgainst(1); checkAgainst < arrayLength; ++ checkAgainst) 
    if(array[checkAgainst] > array[arrayIndex])
      arrayIndex = checkAgainst;

  return(array[arrayIndex]);
}
  
