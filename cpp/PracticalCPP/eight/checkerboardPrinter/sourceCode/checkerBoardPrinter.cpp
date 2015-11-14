/*
 * checkerBoardPrinter--
 *   Prints out a checkerboard of the giobven dimesnions of the user to the 
 *   user.
 * 
 * Author: Luis Perez
 *
 * Purpose: Continued use of new more advanced branch constructs.
 * 
 * Usage: 
 *   User inputs the needed dimensions for the checkerboard. 
 *   Checkerboard of that dimension is output to the user.
 */
#include <iostream>

void runCheckerboardPrinter(void);
void printItOut(int input);
void printCols(int dimension);
void printRows(int dimension);

void test();
int main() {
  runCheckerboardPrinter();
  
  return(0);
}

void printItOut(int input) {  
  int temp(input);
  // The manner is orint out the row, and do so recursively.
  while(temp) { // Prints out the needed boxes. Sans the bottom row.
    printRows(input);
    printCols(input);
    --temp;
  } 
  
  // Cannot add the last row of +---+ into it from the get go as that would
  // make things not work in the amnner that they need to.
  printRows(input);
  
}
void runCheckerboardPrinter(void) {
  int inputDimension;
  std::cout <<"Welcome to the checkerboard printer." 
	    << std::endl 
	    << "Please input the dimensions for the box(X by X): ";
  std::cin >> inputDimension;
  printItOut(inputDimension);

}

void printRows(int dimensionIndex) {
  for(int index(0); index<dimensionIndex; ++index)
    std::cout << "+----";
  std::cout << "+" <<std::endl; ;

}
void printCols(int dimensionIndex) {
  // This is the column counter. Controls how many total columns are produced.
  for(int countIndex(0); 
      countIndex < 3; //Creates the three | per colum situation.
      ++countIndex) {

    // produces the needed rows of the columns to the user. 
    for(int internalCounter(0);
	internalCounter <= dimensionIndex;
	++internalCounter)
      std::cout << "|    ";
    std::cout << std::endl; // Every time it goes about produce a new line.
  }	
}
