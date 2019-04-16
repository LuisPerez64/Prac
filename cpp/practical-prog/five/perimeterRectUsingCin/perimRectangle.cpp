//Purpose: Calculate the perimeter of a rectangle itself 
#include <iostream>


int main(){

  std::cout << "Please input the width, and height of the given rectangle: ";
  float width, height; 
  std::cin >> width >> height;

  float perimeter = 2* (width + height);

  std::cout << "The Perimeter of the given rectangle is: " << perimeter <<"."
	    << std::endl;

  return 0;
}
