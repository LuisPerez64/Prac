/*
 * multiplicationTablePrinter --
 *  prints out to the user a multiplication table of their desired length
 *
 * Author: Luis Perez
 *
 * Purpose: Continued use of advanced loop constructs.
 *
 * Usage: 
 *   User inputs the lower, and upper bound that they want to go for.
 *   Outputs to the user a multiplication table of their own construct.
 */

#include <iostream> // std::cout | std::cin
#include <iomanip> // std::setw(width)

void runMultiplicationTablePrinter();
void printOutMultiplicationLine (int startVariable, int finalVariable,
				 int multiplyItBy);

int main() {
  runMultiplicationTablePrinter();

}

void runMultiplicationTablePrinter() {
  int lowerBound(0), upperBound(0); // Boundaries used to create the table
  
  std::cout
    << "Welcome to the multiplication table printer. " << std::endl
    << "Please input the range of the table to print out." << std::endl;
  std::cout 
    << "Lower Bound: ";
  std::cin >> lowerBound;
  std::cout
    << "Upper Bound: ";
  std::cin >> upperBound;
  
  // This is updated to knowwhen the loop should exit. Cannot modify the bound
  // itself as this would cause bad output.
  int tempBound(lowerBound);
  std::cout 
    << std::endl << "Table in range: "<<lowerBound << "-" << upperBound
    << std::endl;

  /*
   * Starts at the lowerBound to alwas produce a proper multiplication table.
   * runs until the tempBound reaches the upper bound then quits.
   * Increments the multiplier and the bound. eachtime printing out a line
   * for the multiplication table in itself.
   */
  for(int multiplyItBy(lowerBound); tempBound <= upperBound;
      ++multiplyItBy, ++tempBound) {
    printOutMultiplicationLine(lowerBound, upperBound, multiplyItBy);
    std::cout << std::endl; // Print out the line for a table look.
  }
}
void printOutMultiplicationLine (int startVariable, int finalVariable,
				 int multiplyItBy) { 
  // Prints the line out to the user. Goes along and multiplies everything by
  for(;startVariable <= finalVariable; ++startVariable)
    std::cout << std::setw(4) // each number holds four digits 
	      << startVariable * multiplyItBy;
}
 
  
