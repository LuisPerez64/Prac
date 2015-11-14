/*
 *Purpose: Receipt tallying program.
 *Implementation: Takes either supply (1) or Meal (2) or Quit (0) as input
 *                Seperates them and tallies up totals for the receipts.
 *Update        : Added the use of a vector to hold the inputted points of
 *                the receipts to that point. Held for validation.
 */
#include <iostream>
#include <vector>

bool notValid(char input);
void receiptTallying(void);
void outputReceipts(std::vector<double>, std::vector<double>,
		    std::vector<double>);

int main(int argc, char* argv[]) {
  receiptTallying();

  return 0;
}

void receiptTallying(void) {
  std::cout << "Welcome to the receipt tallying program.";
  
  // All variables to be used for this point  
  char yayOrNay('q');
  int choice(0);
  bool toggle(true);
  double suppliesTotal(0.0), mealsTotal(0.0), absoluteTotal(0.0);
  double addedAmt(0.0);
  std::vector<double> suppVect, mealVect, absoVect;

  while(true) {
    std::cout << "What would you like to add in?" << std::endl;
 
    if(toggle) { // So as not to reprint the menu past the first time. 
      std::cout<< "Make numerical choices for:" <<std::endl
	       << "(1) Supplies" << std::endl
	       << "(2) Meals" << std::endl
	       << "(0) Quit" << std::endl
	       << "Choice: ";
      toggle = false;
    } else 
      std::cout << "Next Choice: ";
    
    do {
      std::cin >> choice;
      if (choice < 0 or choice > 2) // Erro message  
	std::cout << std::endl << "Please input proper choice (0 -> 2): ";
    } while (choice < 0 or choice > 2); // Error checking point for choices

    if(choice == 0) // Standard break situation choice is exit.
      break;

    std::cout << "Amount of the receipt: ";
    std::cin >> addedAmt;

    // Put everything into the vector that is needed and is meant to be input
    if (choice == 1) {
      suppliesTotal += addedAmt;
      suppVect.push_back(addedAmt);
    } else { // Trickle down choice point goes here.
      mealsTotal += addedAmt;
      mealVect.push_back(addedAmt);
    }
    // Always increment this with the given input.
    absoVect.push_back(addedAmt);
  }
  absoluteTotal = mealsTotal + suppliesTotal;

  std::cout
    << std::endl << std::endl
    << "Supplies : $" << suppliesTotal << std::endl
    << "Meals    : $" << mealsTotal << std::endl
    << "Total    : $" << absoluteTotal << std::endl;

  while (notValid(yayOrNay)) { 
    std::cout << "Would you like to view your receipts input (y / n)?: ";
    std::cin >> yayOrNay;
  }
  
  if (yayOrNay == 'y' or yayOrNay == 'Y')
    outputReceipts(suppVect, mealVect, absoVect);
  
  return;
}

void outputReceipts(std::vector<double> inpOne, std::vector<double> inpTwo,
		    std::vector<double> inpThree) {

  std::cout << "Supplies" << std::endl;
  for (std::vector<double>::iterator inpIter(inpOne.begin());
       inpIter != inpOne.end(); ++inpIter)
    std::cout << *inpIter << "  ";
  std::cout << std::endl <<std::endl;
  
  std::cout << "Meals" << std::endl;
  for (std::vector<double>::iterator inpIter(inpTwo.begin());
       inpIter != inpTwo.end(); ++inpIter)
    std::cout << *inpIter << "  ";
  std::cout << std::endl << std::endl;

  std::cout << "Everything Input" << std::endl;
  for (std::vector<double>::iterator inpIter(inpThree.begin());
       inpIter != inpThree.end(); ++inpIter)
    std::cout << *inpIter << "  ";
  std::cout << std::endl << std::endl;
}

bool notValid(char input) {
  bool result(false);
  if (input != 'y' and input != 'Y' and input != 'n' and input != 'N')
    result = true;

  return(result);
}
