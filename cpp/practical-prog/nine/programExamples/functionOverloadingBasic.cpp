/*
 * functionOverloadingBasic: Shows to the user what function overloading is at
 *  it's core, and the manners in which this could be used to simplify things,
 *  at this level the same could be achieved with the wonderful world of 
 *  templates.
 *
 * Author : Luis Perez/ Steve Oualline.
 *
 * Purpose: Show to the user what function overloading is. Heavily commented
 *  practice program.
 *
 * Usage: No interaction. Print outs.
 */
#include <iostream>

int square(int value);
float square(float value);

int main() {
  int passMeInInt(4);
  float passMeInFloat(3.0);

  // Based on what is passed into the function it knows that it is working with
  // an int or a float, and calls the appropriate function for the user.
  // This is
  std::cout << "The value for the int that is squared is: " 
	    << square(passMeInInt) << std::endl;
  std::cout << "The value for the float that is squared is: " 
	    << square(passMeInFloat) << std::endl;

  return(0);
}

int square(int value) {
  return(value*value);
}

float square(float value) {
  return(value*value);
}
