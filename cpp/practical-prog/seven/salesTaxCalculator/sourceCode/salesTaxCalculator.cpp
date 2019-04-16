/*
 * salesTaxCalculator --
 *   Takes in user input, and produces a post tax applied value to the user
 *
 * Author: Luis Perez
 * Purpose: Program pre-spec manipulation, and familiarization. Practice
 *
 * Usage:
 *   User inputs tax price, per session, and price of the item to apply tax to
 *   Is presented with the taxed total, and asked if they would like to run 
 *   again with that tax value, if not then go to main, and ask if they would 
 *   like to apply a different tax value, and run again or quit?
 */

#include <iostream>
#include <string>

bool amIDone(std::string questionToPose);
void runTaxCalculator(void);
void taxCalculator(float taxValue);

int main(int argc, char* argv[]) {
  runTaxCalculator();
 
  return(0);
}

void runTaxCalculator(void) {
  float taxValue(0.0);
 
 // Question to be asked of the user...
  std::string question;
  question =
    "Would you like to run calculations with another tax value (y/n)?: ";

  std::cout << "Welcome to the sales tax calculator." 
	    << std::endl << std::endl;
  do {
    std::cout << "What is the tax to be applied?: ";
    std::cin >> taxValue;
    taxCalculator(taxValue);

  }while(amIDone(question));
 
  return;
}

void taxCalculator(float taxValue) {
  float result(0.0);
  float internalTaxValue(1 + (taxValue / 100));
  
  std::string question;
  question = 
    "Are you done with these calculations (y/n): ";

  while(true) {
    std::cout << "What is the value to apply the tax to: ";
    std::cin >> result;
    result *= internalTaxValue;
    std::cout.precision(2);
    std::cout << "Value post tax is: $" << std::fixed << result <<std::endl; 
    if(amIDone(question)) // This is reversed a bit... If false then 
      break;
    continue;
  }
}


bool amIDone(std::string question) {
  bool answer(false);
  char internalAnswer('\0');
  
  // Outputs the question to be asked
  std::cout << question;
  do { // Runs until valid answer is supplied.
    // Runs only on 2nd+ go through
    if(internalAnswer != '\0')
      std::cout << std::endl << "Please answer y/n: ";
    std::cin >> internalAnswer;
  }while( (internalAnswer != 'y' and internalAnswer != 'Y') and
	  (internalAnswer != 'n' and internalAnswer != 'N'));
 
 if(internalAnswer == 'y' || internalAnswer == 'Y')
    answer = true;

  return(answer);
}
  
      
