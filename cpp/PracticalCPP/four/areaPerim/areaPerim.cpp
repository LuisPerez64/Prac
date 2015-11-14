/*
 * areaPerim -- Prints out the calculated points below
 *
 * Author: Luis Perez
 * 
 * Purpose: Highlights the differences between integers and floating point nums
 * 
 * Usage: Is called, executes, prints to the screen exits. 
 */

#include <iostream> // std::cout 

int main(){
  //Area calculation within the aspect of an integer
  std::cout << "Area: " << 3 * 5 << std::endl
	    << "Perim: " << 2*(3+5) << std::endl;

  //Area, Perim for a float, no reuse of the function, single functions.
  std::cout << "Area: " << 6.8 * 2.3 << std::endl
	    << "Perim: " << 2 * (6.8 +2.3) << std::endl;

  return(0);
}
