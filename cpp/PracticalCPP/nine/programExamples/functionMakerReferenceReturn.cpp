/*
 * functionmakerReferenceReturn--
 *   A comment heavy program to highlight the return by reference point.
 *   have not done this before so this may in itself be a bit difficult to work
 *   with.
 *
 * Author: Luis Perez
 *
 * Purpose: Highlight the differences that come from passing a value back to 
 *          the function that called it by reference. Array manipulation.
 *
 * Usage: No real user interaction. Array maninpulation.
 */

#include <iostream>

// Simple passByValue point
void incCountValue(int counter);
// Simple passByRefernce Point
void incCountReference(int &counter);

// Main emphasis of this file in itself.  Returns the address of the value.
int& biggest(int array[], int nElements);
// Returns an address to a value, but the addressed value cannot be changed.
const int& min(int array[], int nElements);

int main() {
  /* // Commented out for simplicities sake.
     { // Pass by Value/reference Demonstration.
     std::cout << "Pass by value/reference Demonstration." << std::endl;
    
     int count(1); //Ceases to exist after this point is exemplified.
     std::cout << count << " Before anything is called." << std::endl;
  
     incCountValue(count); // Increments count within the function.
     std::cout << count << " After incCountValue."  << std::endl;
  
     incCountReference(count);
     std::cout << count << " After incCountReference." << std::endl;
     }
  */


  { std::cout <<"Reference as the return value Program." <<  std::endl;
    
    int arrayOfInts[5]; // An array of five integers.
    
    // Place in the values 1 - 5 into the array at the indexed locations.
    for(int arrayIndexCounter(0); arrayIndexCounter < 5; ++arrayIndexCounter)
      arrayOfInts[arrayIndexCounter] = (arrayIndexCounter + 1);
    
    // Prints out 5, as the element that is the biggest in the array.
    std::cout << "Biggest element in the array is: " 
	      << biggest(arrayOfInts, 5) << "." << std::endl;

    /* 
       Since we are returning the addres of a variable within an array, we can
       instantly change this value, into whatever we want so this changes the 
       value within the array into the number that we dictate it to be.
    */
    biggest(arrayOfInts, 5) = 123;
    // Biggest is now 123.
    std::cout << "Biggest element in the array after change is: " 
	      << biggest(arrayOfInts, 5) << "." << std::endl;
  
    std::cout << "Now dealing with the minimum values in the array." 
	      << std::endl;
    std::cout << "The smallest element in the array is " << min(arrayOfInts, 5)
	      << std::endl;
    
    std::cout 
      << "Since min passes back a const reference, it cannot be"
      << std::endl << "changed in the same manner, as biggest value."
      << std::endl;
    /*
      This will yield a simple compilation error. This cannot work because
      the referenced point cannot be changed as it has been flagged as a 
      const variable. The address point can still be altered directly within
      the array, but not with this form:
      
      // This will not work.
      min(arrayOfInts, 5) = 12;
    */
  }

  return(0);
}

/*
 * Returns a pointer to an element in an integer array.
 * Takes in an array, and the size of the array, number of elements as it's 
 *  parameters.
 */
int& biggest(int array[], int nElements) {
  // The index point of largest point to be returned to the caller.
  // Initialized at 0 to point otthe beginnning of the array that is passed.
  int biggest = 0; 
  
  // The comparison Index within the array.
  for(int index(1); index < nElements; ++index)
    // Basic comparison of the elements. If the next element tested against is
    // bigger than the one pointed to by biggest at the time. Take that as the 
    // new index point of biggest, and point to that elt.
    if(array[biggest] < array[index])
      biggest = index;

  // Return the address of the element that is being pointed to by the array.
  return(array[biggest]);
}

/*
 * Returns an unchangeable pointer address to the caller, of the smallest elt
 * int the given array.
 * Parameters: An array of integers, and the number of elts in the array.
 */
const int& min(int array[], int nElements) {
  int minIndex = 0; // Start it at the begining of the array.
  
  // Starts to iterate through the array, and finds the pointer to the smallest
  // indexed element.
  for(int arrayIndex(1); arrayIndex < nElements; ++arrayIndex)
    if(array[minIndex] > array[arrayIndex])
      minIndex = arrayIndex;

  return(array[minIndex]); // Returns the arrayIndex to the smallest variable in the
  // array. This number cannot be changed as the result of this function.
}
void incCountValue(int counter) {
  ++counter; // Does not reflect on the caller functions parameters.
}

void incCountReference(int &counter) {
  ++counter; // Does reflect on the caller functions parameters.
}
