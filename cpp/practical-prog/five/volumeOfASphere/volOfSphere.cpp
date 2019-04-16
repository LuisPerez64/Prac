//Purpose: Calculation of the volume of a spheroid
#include <iostream>
#include <cmath>

const float PI = 3.14159;
int main(){
  
  std::cout << "What is the radius of the sphere in question?: ";
  float sphereRadius;
  std::cin >> sphereRadius;
  
  float volume;
  volume = (4.0/3.0) * PI * std::pow(sphereRadius, 3);
  
  std::cout << "The volume of a sphere with radius "<< sphereRadius << " "
  << "is " << volume << "." << std::endl;

  return 0;
}
