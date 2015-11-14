//Purpose: Calculation of the leap year functionality
#include <iostream>

int main(){
  int year;
  bool leapYear = false;

  std::cout << "What year would you like to check?: ";
  std::cin >> year;

  if( (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)) ) 
    leapYear = true;
  //Else Leap Year is false as initiated.

  if(leapYear)
    std::cout << "The year " << year << " is a leap year." <<std::endl;
  else 
    std::cout << "The year " << year << " is not a leap year." << std::endl;

  return 0;
}
