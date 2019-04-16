//Purpose: The conversion of kilomeeter per hour to miles per hour.
#include <iostream>

int main(){

  std::cout << "How mnay Kilometers per hour are you traveling?: ";
  float kilos;
  
  std::cin >> kilos;

  float miles = kilos * 0.6213712;
  
  std::cout << "This equates to " << miles << " miles per hour." << std::endl;

  return 0;
}
