/* 
 * functionMaker -- Practice program for functions, and how they're structured.
 *
 * Author: Luis Perez
 *
 * Purpose: Highlight diffrent types of functions, and what they do. Comment 
 *          havy.
 *
 * Usage: Practice Program. No real interface with the user.
 */

#include <iostream>

//Is handed a width and a height by the user, returns the area of thetriangle.
int triangleBasic(int width, int height);

const int triangleBasicConst(const int width, const int height);

int triangleBasicReference(int &width, int &height);

const int triangleBasicsConstReference(const int &width, const int &height);

void triangleBasicsReferenceVoide(int &width, int &height);

int main() {
  int width, height; // Width and height used for a triangle.
  std::cout << "Please input width and height of the triangle: ";
  std::cin >> width >> height;

  // This is strictly passed by value. Any changes that occur to this functions
  // Parameters, are with the copies that are handed to it. It does not change
  // This functions actual width/height.
  std::cout << "Triangle Basic: " 
	    << triangleBasic(width, height) << std::endl;
  std::cout << "Width: " << width << " Height: " << height << std::endl;
  
  // This is a hardwirded function. The values are passed by value again, but
  // They cannot be changed directly within the function. This would be wanted
  // in a function that does what this one does. Multiply users input.
  std::cout << "Triangle Basic Const: " 
	    << triangleBasicConst(width, width) << std::endl;
  std::cout << "Width: " << width << " Height: " << height << std::endl;
 
  // Here is where things start getting a bit hectioc. The coder passes in the
  // Addresses of the variables. This is then changed within the function, with
  // the added functionality of changing the actual variables themselves. Now
  // from here forward the function runs with the variables width/height 
  // changed into whatever they were changed into in the function itself.
  std::cout << "Triangle Basic Reference: " 
	    << triangleBasicReference(width, height) << std::endl;
  std::cout << "Width: " << width << " Height: " << height << std::endl;
 
  // Passing in the address of the variables once again, but this time we have
  // only got a handle to see and use the variable. We cannot change it. We 
  // can make a temporary hodler variable and do with it what we need, but
  // from the functions perspective, what comes in is what comes out.
  std::cout << "Triangle Basic Const Reference: "
	    << triangleBasicsConstReference(width, height) << std::endl;
  std::cout << "Width: " << width << " Height: " << height << std::endl;
  
  // Calling the function here as it returns void.
  // This function was written to exemplify the point that the functions once
  // called with references to the variables that called them, have full 
  // ability to change the variables from the scope of the function that called
  // them. Now the values in width height have been changed from within the
  // function, and reflect the change to the user here.
  triangleBasicsReferenceVoide(width, height);
  std::cout << "Triangle Basic Reference Void: Width and Height changed.: " 
	    << std::endl  
	    << "Width: " << width  << " Height: " << height << std::endl;  
  return(0);
}

// The basic formula.
int triangleBasic(int width, int height) {
  /* 
     Can change any of the values that are brought in directly.
      width = 10000;
      height = 1;
  */
  width = 50;
  height = 20;
  return(width * height);
}

// Can't change any of the values.
const int triangleBasicConst(const int width, const int height) {
  /*
    Yields an error if this is tried:
      width = 100;
      height = 1000;
  */
  return(width * height);
}

// Value changes reflect on the caller parameters themselves.
int triangleBasicReference(int &width, int &height) {
  /* 
     Changes the actual values within width and height for the functions after
     this has been called..
  */
  width = 100;
  height = 50;
  return(width * height);
}

// Can't change anything within the function itself.
const int triangleBasicsConstReference(const int &width, const int &height) {
  /*
    Yields an error if this is tried:
     width = 30;
     height = 22;
  */
  int tempWidth = width; // Now the value can be manipulated with the handle
  return(width * height);
}
  
// Just here to show that changes made to the reference variable are reflected.
// Not really needed, as the point is made above, but repetition...
void triangleBasicsReferenceVoide(int &width, int &height) {
  std::cout << "Input new Width and Height: ";
  std::cin >> width >> height;

}
