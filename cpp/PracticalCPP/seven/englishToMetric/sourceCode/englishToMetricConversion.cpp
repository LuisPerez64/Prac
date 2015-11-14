/*
 * englishToMetric - COnversion of english measurements to metric measurements
 *    Basic at this level, will be enhanced later on.
 *
 * Author: Luis Perez
 * Specs: Documentation folder, Program Specs Highlights most ecerything.
 *
 * Usage: 
 *  User is prompted with the type of data that they would like to convert.
 *  User inputs the units to be converted. 
 *  Program outputs the converted unit after conversion calculator.
 *  Loops as long as the user wishes.
 */

#include <iostream>
#include <string>
#include "englishToMetric.hpp"

int main(int argc, char **argv) {
  // Nothing needs to be initialized.
  std::cout << "Welcome to the conversion program." << std::endl << std::endl;
  while(true) { // Run as long as the user wishes.
    if(! runConverter() ) // Break if the user no longer wants to run me.
      break;
  }

  return(0);
}

bool runConverter(void) {
  inputOutput(); // Runs this, and goes forth with end user interaction.

  bool runMeAgainBool(true); // Value to be returned, dictates redo of the loop
  char runMeAgain('\0'); // Input from the user, used to fill in above Bool
  // Runs to see if the user would like to do this stuff all over again.
  std::cout << "Would you like to convert something else (y/n)?: ";
 
  while(validityCheck(runMeAgain)) {   
    if(runMeAgain != '\0') // Runs after the first time runMeAgain is filled
      std::cout << "Please use valid input: y/n: ";
    std::cin >> runMeAgain; //Get input from the user, if not valid run again.
  }
  if(runMeAgain == 'n' || runMeAgain == 'N')
    runMeAgainBool = false;

  return runMeAgainBool;
}

void inputOutput(void) {
  int conversionChoice(-1); // Holds the users choice in conversion scheme
  float numberToConvert(0.0); 

  std::cout << "What would you like to convert?:" << std::endl;
  do {
    std::cout << "(0) Quit" << std::endl
	      << "(1) Distances Conversion" << std::endl
	      << "(2) Weights Conversion" << std::endl
	      << "(3) Volumes Conversion" << std::endl << std::endl;
    std::cout << "Choice: ";
    std::cin >> conversionChoice;
  }while(conversionChoice < 0 or conversionChoice > 3);
  if(conversionChoice == 0)
    return;

  std::string inputConversionType, outputConversionType;
  outputStringAssigns(conversionChoice,
		      inputConversionType, outputConversionType);
    
  std::cout << "How many " << inputConversionType 
	    << " would you like to convert to " << outputConversionType <<": ";
  std::cin >> numberToConvert;
  // Conversion to make this canonical english. Same below.
  // Removes the 's' from the string, to make it singular.
  if(numberToConvert == 1.0 or numberToConvert == -1.0)
    inputConversionType = 
      inputConversionType.substr(0, inputConversionType.length() - 1);
  
  float convertedNumber(doConversion(conversionChoice, numberToConvert));   
  if(convertedNumber == 1.0 or convertedNumber == -1.0)
    outputConversionType =
      outputConversionType.substr(0, outputConversionType.length() - 1);

  std::cout << numberToConvert << " " << inputConversionType 
	    << " is equal to " << convertedNumber << " " 
	    << outputConversionType << "." << std::endl << std::endl;
}


float doConversion(const int &conversionChoice, const float &numberToConvert) {
  float convertedValue(numberToConvert);

  switch(conversionChoice){
  case 1: // Convert miles to kilometers.
    convertedValue *= 1.609344;
    break;
  case 2: // Convert pounds to kilograms.
    convertedValue *= 0.453592;
    break;
  case 3: // Convert gallons to liters.
    convertedValue *= 3.78541;
    break;
  default: // Should never get here but again... Never happens too often.
    break;
  }

  return(convertedValue);
}

inline bool validityCheck(const char &input) {
  bool isNotValid(false);
  if((input != 'y' and input != 'Y') and
     (input != 'n' and input != 'N'))
    isNotValid = true;

  return isNotValid;
}

void outputStringAssigns(const int &conversionChoice,
			 std::string &inputConversionType,
			 std::string &outputConversionType) {

  switch(conversionChoice) {
  case 0: // Quit 
    return;
  case 1: // Distances
    inputConversionType = "Miles"; 
    outputConversionType = "Kilometers";
    break;
  case 2: // Weights
    inputConversionType = "Pounds";
    outputConversionType = "Kilograms";
    break;
  case 3: // Volumes
    inputConversionType = "Gallons";
    outputConversionType = "Liters";
    break;
  default: // Should never get here, but... Never say never right -_-
    break;
  }

  return;
}
