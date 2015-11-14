/*
 * numbersToNormalizedWords
 *  Takes in a user input number ie. 99 produces the normalized english
 *  spelling of the number to the user.
 *
 * Author: Luis Perez
 *
 * Purposed: 
 *  Continued review of some of the advanced flow control statements. 
 *
 * Usage:
 *   input the number to be converted into its written form, in basic english.
 */

#include <iostream>
#include <string>

std::string convertTheNumberToEnglish(int);
std::string returnedStringFunct(int);
int findValue(int);
int numberToBePrinted(int& inputNumber, int rangeCheck); 
void runNumbersToNormalizedWords(void);
int rangeFinder(int inputNumber);

//void test();

int main() {
  //  test();
  runNumbersToNormalizedWords();
  
  return(0);
}

void runNumbersToNormalizedWords(void) {
  int numberToBeConverted(0);
  std::string convertedNumberInAlpha;
  
  std::cout 
    << "What number would you like to convert into normalized english: ";
  std::cin >> numberToBeConverted;
  
  convertedNumberInAlpha = returnedStringFunct(numberToBeConverted);
  
  std::cout 
    << numberToBeConverted << " is " << convertedNumberInAlpha << std::endl;
}

// Ug;y form... No recursive calls. Straight iterative?
std::string convertTheNumberToEnglish(int inputNumber) {
  std::string returnString;
  
  return(" "); // Empty tab return.
}

std::string returnedStringFunct(int inputNumber) {
  std::string returnedString;
  
  // while(inputNumber != 0) {
    if(inputNumber < 20)
      switch(inputNumber) {
      case 1:
	returnedString += "one";
	break;
      case 2:
	returnedString += "two";
	break;
      case 3:
	returnedString += "three";
	break;
      case 4:
	returnedString += "four";
	break;
      case 5:
	returnedString += "five";
	break;
      case 6:
	returnedString += "six";
	break;
      case 7:
	returnedString += "seven";
	break;
      case 8:
	returnedString += "eight";
	break;
      case 9:
	returnedString += "nine";
	break;
      case 10:
	returnedString += "ten";
	break;
      case 11:
	returnedString += "eleven";
	break;
      case 12:
	returnedString += "twelve";
	break;
      case 13:
	returnedString += "thirteen";
	break;
      case 14:
	returnedString += "fourteen";
	break;
      case 15:
	returnedString += "fifteen";
	break;
      case 16:
	returnedString += "sixteen";
	break;
      case 17:
	returnedString += "seventeen";
	break;
      case 18:
	returnedString += "eighteen";
	break;
      case 19:
	returnedString += "nineteen";
	break;
      default:
	break;
      } // Runsoff at this, no functions called after this.
    else if(inputNumber < 100) {
      // Value will be a number which mod 10 == 0 ie 20,30...,90
      switch(findValue(inputNumber)) { 
      case 20:
	returnedString += "twenty ";
	break;
      case 30:
	returnedString += "thirty ";
	break;
      case 40:
	returnedString += "fourty ";
	break;
      case 50: 
	returnedString += "fifty ";
	break;
      case 60:
	returnedString += "sixty ";
	break;
      case 70:
	returnedString += "seventy ";
	break;
      case 80:
	returnedString += "eighty ";
	break;
      case 90:
	returnedString += "ninety ";
	break;
      default:
	break;
      }
      returnedString += 
	returnedStringFunct(inputNumber % rangeFinder(inputNumber));
      // continue; // Goes back to the beginning while loop print out remainder
    } else if(inputNumber < 1000) {
      // attain the first digit in the hundreds place
      int tempInput(inputNumber / rangeFinder(inputNumber));
      
      // feed that back into the function. ie one + " hundred" is now within 
      // the returnedString.
      returnedString += returnedStringFunct(tempInput) + " hundred "; 
      
      // Now do the basic point and get the rest of the words in the string
      // recursively.
      returnedString += 
	returnedStringFunct(inputNumber % rangeFinder(inputNumber));
    }
    
 // } 
  return(returnedString);
  
}

/************************* Tested Functions ***************************/
/* Note
 * The number that is to be placed back into the inputNumber field is in itself
 * the modulo remainder of the initial number against the range we are
 * currently checking. This is because we read numbers from the greatest value
 * marker to the least significant one. So we would get the numbers 1 2 3 4 5
 * as returns if we fed in 12345, instead of 5 4 3 2 1. This facilitates the 
 * implementation that I am going for with a comounding string being what is 
 * handed back to the user.
 */ 
// Does what is needed
// This is what is most of all done with the two functions below... Except iy
// updates the input for you internally... aka complications, 
int numberToBePrinted(int& inputNumber, int rangeCheck) {
  int returnValue; // The number that is to be printed to the user.
  int temp(inputNumber % rangeCheck); // Get the remainder after the rangeCheck
  
  inputNumber -= temp; // Get the barebone number to print in relation to range
  returnValue = inputNumber / rangeCheck;
  
  inputNumber = temp; // The remainderis what is left.
  return(returnValue);
}

// Used with the findValue function.
int rangeFinder(int inputNumber) {
  int returnValue(1); // Returns the number to be used in the modulo function. 
 
  for(/* */; (returnValue*10) <= inputNumber; returnValue *=10);
  
  return(returnValue);
}
 
int findValue(int input) {
  //attain the remainder of the input number once its been moduloed.
  int tempValue(input % rangeFinder(input)); 
  // Take that value andsubtract it from the input number. ie.
  // input = 123 after this is run tempValue = 100, whichis used in the switch
  // statements, instead of nest if-elseifs.
   tempValue = input - tempValue;
  
  return tempValue;
}
