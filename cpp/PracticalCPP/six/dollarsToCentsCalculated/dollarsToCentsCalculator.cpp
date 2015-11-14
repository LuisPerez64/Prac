//Purpose: Simulates a change machine, and moves forward in itself
#include <iostream>

int main(){
  float moneyPutIn; //The money that will be converted to dollars and cents;
  int quarters, dimes, nickels, pennies;//The to be converted points;
  quarters = dimes = nickels = pennies = 0; //Chain assignment, not too good...

  std::cout << "How much money would you like to get changed?: ";
  std::cin >> moneyPutIn;
 
  while(moneyPutIn > 0){
    
    if(moneyPutIn >= 0.25){
      ++quarters;
      moneyPutIn -= 0.25;
    }else if(moneyPutIn >= 0.10){
      ++dimes;
       moneyPutIn -= 0.10;
    }else if(moneyPutIn >= 0.05){
      ++nickels;
      moneyPutIn -= 0.05;
    } else{ 
      ++pennies;
      moneyPutIn -= 0.01;
    }
  
  }

  std::cout << "For the money put in you get:" <<std::endl
	    << "Quarters: " << quarters <<std::endl
	    << "Dimes:    " << dimes <<std::endl
	    << "Nickels:  " << nickels <<std::endl
	    << "Pennies:  " << pennies <<std::endl;

  return 0;
}
