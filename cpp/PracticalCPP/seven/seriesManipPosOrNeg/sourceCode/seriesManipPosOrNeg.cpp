/*
 * SeriesManipPosOrNeg
 *   Counts the number of negatve and positive numbers that occur within the 
 *   given boundaries of basic user input.
 *
 *  Author: Luis Perez
 *  Purpose: Introduction of basic if/else. 
 *           Use of the <random> library, haven't used it before.
 *           Basic vector manipulation again, simple efficient, no need to 
 *            use a set at the time. This will be rather simple.
 *
 *  Usage:
 *    User inputs the total number of items that they would like to bring in
 *    as the amount of items that are being counted increases, the numbers of 
 *    both the given types (+/-) should approach 50/50. 
 *    After the user inputs the number of items to validate, outputs the amount
 *    of each type of item that is within the given vector.
 */

#include <iostream>
#include <vector>
#include <random>


int main() {
  std::random_device randomInput;
  int pos(0), neg(0), amountOfSeries(0);  

  std::cout << "How many numbers would you like to simulate?: ";
  std::cin >> amountOfSeries;
  for(int i(0); i <= amountOfSeries; ++i)
    if (randomInput() % 2 == 0)
      ++pos;
    else
      ++neg;

  std::cout << "Negatives: " << neg << " Positives: " << pos <<std::endl;
}  
  
