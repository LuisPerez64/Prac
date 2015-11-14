//Purpose: Changing over the minutes to hours, and minutes themselves;

#include <iostream>

int main(){

  std::cout << "How many minutes are going into this calculation?: ";
  int minutes;
  std::cin >> minutes;
  int hours = minutes / 60;//Normal division to attain the hours, truncated.
  minutes %= 60;//Modular division to attain the amount of minutes left after
                //the given hours.
  
  std::cout << "This equates to " << hours << " hours and " << minutes 
	    << " minutes." << std::endl;


  return 0;
}
