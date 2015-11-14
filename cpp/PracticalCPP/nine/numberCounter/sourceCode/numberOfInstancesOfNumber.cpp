/*
 * numberOfInstancesOfNumber:
 *  Is given an array, and a number to check for in the array. Takes that and
 *  relays to the user the amount of times that the number has occured in the 
 *  array.
 *
 * Author: Luis Perez
 * 
 * Purpose: 
 *  Array manipulation. Functional programming practice.
 *
 * Usage:
 *  User inputs numbers into an array. The array is then checked for a specific
 *  number, the amount of times that number is met is recorded, and relayed to
 *  the caller.
 */
#include <iostream>

void runNumberOfInstancesOfNumber(void);
int numberOfTimesNumberAppears(int number, int array[], int arrayLength);
const int ARRAY_LENGTH = 10; 

int main() {
  runNumberOfInstancesOfNumber();
  return(0);
}

void runNumberOfInstancesOfNumber(void) {
  int arrayOfInts[ARRAY_LENGTH];
  int numberToLookFor(0);
  int inputNumber; // Number to be placed into the array
  std::cout << "Welcome to the number of instances counter." << std::endl;
  std::cout << "Begin input of numbers into the array." << std::endl;

  // Input numbers into the array, based on the length of the array.
  for(int inputIndex(0); inputIndex < ARRAY_LENGTH; ++inputIndex) {
    std::cout << "Number to add to array: ";
    std::cin >> inputNumber;
    arrayOfInts[inputIndex] = inputNumber;
  }

  std::cout << "What number would you like to look for: ";
  std::cin >> numberToLookFor;

  std::cout 
    << "Number of times that " << numberToLookFor<<" appears in the array is: "
    << numberOfTimesNumberAppears(numberToLookFor, arrayOfInts, ARRAY_LENGTH) 
    << std::endl;
}

/*
 * The array is searched, always verifying the last value, at array length.
 * If the value at the end of the array is equal to the number searched for
 * then increment the tally, and make the call recursively to the function.
 * When making the call everything stays the same, the value that changes 
 * is the array length, which is decremented by one to change the index at 
 * each recursive call. Once the array length is at 0, then break away fully.
 */
int numberOfTimesNumberAppears(int number, int array[], int arrayLength) {
  if(arrayLength == 0) // Break point so array length could not be negative.
    // Array is at an end. Add 0 to the total. Break case.
    return 0;
  
  // The arrayLength -1 point is searched because the arrays length initially
  // would be out of bounds for the first run through.
  if(array[arrayLength -1] == number) // Number sought is found.
    // Recursive call with the number count being incremented.
    return(1 + numberOfTimesNumberAppears(number, array, arrayLength -1));
  else // Number not found
    // recursive call with nothing being added to running tally.
    return(numberOfTimesNumberAppears(number, array, arrayLength - 1));
}
      
