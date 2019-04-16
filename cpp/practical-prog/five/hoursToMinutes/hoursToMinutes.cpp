//Purpose: Conversion of hours to minutes fir whatever needed reason

#include <iostream>

int main(){

  std::cout << "How many hours are we talking about here?: ";
  int hours; 
  std::cin >> hours;
  std::cout << "And how many minutes are we taking into account: ";
  int minutes;
  std::cin >> minutes;
  
  minutes+= (hours * 60);//Gets the minutes from the hours, and adds to minutes
  
  std::cout << "That comes out to " << minutes << " minutes total." 
	    << std::endl;
  
  return 0;

}
