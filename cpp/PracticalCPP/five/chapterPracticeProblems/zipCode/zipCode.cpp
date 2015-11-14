#include <iostream>

long int zip;

int main(){

  zip = 0x02137L;

  std::cout << "Zip code for New York is: " << static_cast<int>(zip) << std::endl;
  return 0;
}
