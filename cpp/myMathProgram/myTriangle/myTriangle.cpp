#include <iostream>
#include <cmath> // trig functions importing
#include "myTriangle.hpp"

const float PI=3.14159265359; // Approximation of PI
#define degrees *PI/180 // When using the trig functs convert to degrees
const int AMOUNT_OF_VARIABLES = 10;
int main() {
  Triangle inputTriangle;
  inputTriangle.printOutAllValues();
}

void Triangle::getUserKnownValues() {
  bool printMenu(true); // Manages display of the menu for the user.
  int userChoice(NULL); // The value that the user knows is selected here.
  char userInputShowMenu('\0'); // Used to toggle the showing of the menu.

  while(true) {
    if(printMenu) {
      printUserKnownValuesMenu();
      printMenu = false;
    }

    std::cout
      << "Please make choice (Zero to exit input sequence): ";
    std::cin >> userChoice;
    if(userChoice == 0)
      break;
    inputKnownValue(userChoice);

    std::cout << "Would you like to view the menu? (Y/N): ";
    std::cin >> userInputShowMenu; // Users toggle point
    if(userInputShowMenu == 'y' or userInputShowMenu == 'Y')
      printMenu = true;

    std::cout << "Would you like to view the input values so far? (Y/N): ";
    std::cin >> userInputShowMenu; // reuse the user toggle point.
    if(userInputShowMenu == 'y' or userInputShowMenu == 'Y') {
      std::cout << std::endl << std::endl;
      printOutAllValues(); // If the user wants to view their input so far.
    }
  }

  std::cout << "If at least two points are known then this should work";
}

/*
  NOTE:
   Add a way for the user to remove their input if they placed in a wrong value
   This is as simple as checking if it's known, and adding a simple prompt, may
   be a function with the boolean.
*/
void Triangle::inputKnownValue(int userChoice) {
  int internalUserChoice(NULL); // Users choice for in switch branching.

  switch(userChoice) {
  default:
    std::cout
      << std::endl << "That's not a valid choice." << std::endl << std::endl;
    break;

  case 1:
    if(isHYPKnown) // If the value has already been defined.
      wrongInputValue(isHYPKnown, HYP); // Call the function to right the wrong
    else { // Else first time value is being input.
      std::cout
	<< "Input the length of the Hypotenuse: ";
      std::cin >> HYP;
      wasInputValueKnown(isHYPKnown); // Set the toggle for this value.
    } break;

  case 2:
    if(isOPPKnown)
      wrongInputValue(isOPPKnown, OPP);
    else {
      std::cout
	<< "Input the length of the Opposite Side: ";
      std::cin >> OPP;
      wasInputValueKnown(isOPPKnown);
    } break;

  case 3:
    if(isADJKnown)
      wrongInputValue(isADJKnown, ADJ);
    else {
      std::cout
	<< "Input the length of the Adjacent Side: ";
      std::cin >> ADJ;
      wasInputValueKnown(isADJKnown);
    } break;

  case 4:
    if(isAngleThetaKnown)
      wrongInputValue(isAngleThetaKnown, angleTheta);
    else {
      std::cout //Need to convert if not in degree's
	<< "Is angle theta in Degrees or Radian?" << std::endl
	<< "(1) Degrees \n (2) Radians" << std::endl;

      // Just loops to make sure that a valid choice is made by the user.
      while(internalUserChoice != 1 and internalUserChoice != 2){
	std::cout
	  << "Input Choice: ";
	std::cin >> internalUserChoice;
      } // Change the conversion factor, but not applicable anywhere else atm.
      if(internalUserChoice == 1)
	isInputInDegrees = true;

      std::cout
	<< "Please input the angle. (If not degree's will be converted): ";
      std::cin >> angleTheta;
      if(!isInputInDegrees) // If in radians convert to degree's
	angleTheta *= 180 / PI;

      wasInputValueKnown(isAngleThetaKnown);
    } break;

  case 5:
    if(isSineKnown)
      wrongInputValue(isSineKnown, sineTheta);
    else {
      std::cout
	<< "Input Sine Theta: ";
      std::cin >> sineTheta;
      wasInputValueKnown(isSineKnown);
    } break;

  case 6:
    if(isCosineKnown)
      wrongInputValue(isCosineKnown, cosineTheta);
    else {
      std::cout
	<< "Input Cosine Theta: ";
      std::cin >> cosineTheta;
      wasInputValueKnown(isCosineKnown);
    } break;

  case 7:
    if(isTangentKnown)
      wrongInputValue(isTangentKnown, tangentTheta);
    else {
      std::cout
	<< "Input Tangent Theta: ";
      std::cin >> tangentTheta;
      wasInputValueKnown(isTangentKnown);
    } break;

  case 8:
    if(isCosecantKnown)
      wrongInputValue(isCosecantKnown, cosecantTheta);
    else {
      std::cout
	<< "Input Cosecant Theta: ";
      std::cin >> cosecantTheta;
      wasInputValueKnown(isCosecantKnown);
    } break;

  case 9:
    if(isSecantKnown)
      wrongInputValue(isSecantKnown, secantTheta);
    else {
      std::cout
	<< "Input Secant Theta: ";
      std::cin >> secantTheta;
      wasInputValueKnown(isSecantKnown);
    } break;

  case 10:
    if(isCotangentKnown)
      wrongInputValue(isCotangentKnown, cotangentTheta);
    else {
      std::cout
	<< "Input Cotangent Theta: ";
      std::cin >> cotangentTheta;
      wasInputValueKnown(isCotangentKnown);
    } break;
  }
}

void Triangle::wasInputValueKnown(bool &inputBoolean) {
  if(inputBoolean == false) // Placed here to not allow double known values
    ++knownCount; // Only make it known if the user hasn't made it known before
  inputBoolean = true;
}

/*
  Pseudo:
   If the user has placed in a wrong variable, then reset the the known counter
   Reset the boolean to false, just in case they just don't know it.
   Place the Default NULL value in the container, variable itself.
   Ask the user if they know the value, if they don't then just return forward.
   This function gets called only if the value is stated as known in the bool.
*/
void Triangle::wrongInputValue(bool &inputBoolean, float &inputContainer) {
  inputBoolean = false; // Set the known value to false Just in Case
  --knownCount; // Decrement the amount of values that are known.
  char usersCharChoice('\0'); // Y/N toggle for new known input

  std::cout
    << "You've input this variable before with the value " << inputContainer
    << " ." << std::endl;

  std::cout
    << "Do you know the value to be input? (Y/N): ";
  std::cin >> usersCharChoice;
  if(usersCharChoice == 'y' or usersCharChoice == 'Y') {
    std::cout << std::endl << "Please input new value: ";
    std::cin >> inputContainer;
    ++knownCount; // Reverse the changes made here.
    inputBoolean = true;
  } else {
    inputContainer = NULL;
    std::cout
      << "Container has been reset, and the value is now unknown."
      << std::endl;
  }
}

void printUserKnownValuesMenu() {
  std::cout // May split into multiple branched statements in the future.
    << "Please input points of the triangle that are known. " << std::endl
    << "Select Number Associated with known Value:" << std::endl
    << "(0) None Known" << std::endl << std::endl

    << "Length of sides" << std::endl
    << "(1) Hypotenuse" << std::endl
    << "(2) Opposite" << std::endl
    << "(3) Adjacent" << std::endl << std::endl

    << "Trigonometric Points" << std::endl
    << "(4) Angle Theta" << std::endl
    << "(5) Sine Theta" << std::endl
    << "(6) Cosine Theta" << std::endl
    << "(7) Tangent Theta" << std::endl
    << "(8) Cosecant Theta" << std::endl
    << "(9) Secant Theta" << std::endl
    << "(10) Cotangent Theta" << std::endl << std::endl;
}

// Initializing all the known or now points.
void Triangle::calculateAllValuesInDegrees() {

  calculateTrigIdentities();
  calculateLengths();
  std::cout << "Known Count: " << knownCount << std::endl;
}

void Triangle::calculateLengths() {
  // Calculate the Hypotenuse
  if(!isHYPKnown) {
    float temp = HYP;
    if(isOPPKnown and isADJKnown)
      HYP = sqrt(pow(ADJ, 2) + pow(OPP, 2));

    if(temp != HYP) {
      isHYPKnown = true;
      ++knownCount;
    }
  }

  // Calculate the Opposite
  if(!isOPPKnown) {
    float temp = OPP;
    if(isHYPKnown and isADJKnown)
      OPP = sqrt(pow(HYP, 2) - pow(ADJ, 2));

    if(temp != OPP) {
      isOPPKnown = true;
      ++knownCount;
    }
  }

  // Calculate the Adjacent
  if(!isADJKnown) {
    float temp = ADJ;
    if(isOPPKnown and isHYPKnown)
      ADJ = sqrt(pow(HYP, 2) + pow(OPP, 2));

    if(temp != ADJ) {
      isADJKnown = true;
      ++knownCount;
    }
  }
}

void Triangle::calculateTrigIdentities() {
  // Calculate angle Theta
  if(!isAngleThetaKnown) {
    float temp = angleTheta;
    // If any of the trig identities are known.
    if(isSineKnown)
      angleTheta = asin(sineTheta);
    else if(isCosineKnown)
      angleTheta = acos(cosineTheta);
    else if(isTangentKnown)
      angleTheta = atan(tangentTheta);

    if(temp != angleTheta) {
      isAngleThetaKnown = true;
      ++knownCount;
    }
  }

  // Calculate Sine(theta)
  if(!isSineKnown) {
    float temp = sineTheta; // So as not to have to validate every time.
    if(isAngleThetaKnown)
      sineTheta = sin(angleTheta degrees);

    if(temp != sineTheta) {// The value in sineTheta's been changed to a known.
      isSineKnown = true;
      ++knownCount;
    }
  }
  // Calculate Cosine(theta)
  if(!isCosineKnown) {
    float temp = cosineTheta;
    if(isAngleThetaKnown)
      cosineTheta = cos(angleTheta degrees);

    if(temp != cosineTheta) {
      isCosineKnown = true;
      ++knownCount;
    }
  }

  // Calculate Tangent(theta)
  if(!isTangentKnown) {
    float temp = tangentTheta;
    if(isAngleThetaKnown)
      tangentTheta = tan(angleTheta degrees);

    if(temp != tangentTheta) {
      isTangentKnown = true;
      ++knownCount;
    }
  }


  // Calculate Secant(theta)
  if(!isSecantKnown) {
    float temp = secantTheta;
    if(isCosineKnown)
      secantTheta = 1 / cosineTheta;

    if(temp != secantTheta) {
      isSecantKnown = true;
      ++knownCount;
    }
  }

  // Calculate Cosecant(theta)
  if(!isCosecantKnown) {
    float temp = cosecantTheta;
    if(isSineKnown)
      cosecantTheta = 1 / sineTheta;

    if(temp != cosecantTheta) {
      isCosecantKnown = true;
      ++knownCount;
    }
  }

  // Calculate Cotangent(theta)
  if(!isCotangentKnown) {
    float temp = cotangentTheta;
    if(isTangentKnown)
      cotangentTheta = 1 / tangentTheta;

    if(temp != cotangentTheta) {
      isCotangentKnown = true;
      ++knownCount;
    }
  }
}

// Prints out to the user all the values held in the triangle.
void Triangle::printOutAllValues() {
  std::cout
    << "Values held in this triangle: " << std::endl
    << "Known Lengths " << std::endl
    << "Length Hypotenuse: " << HYP << std::endl
    << "Length Opposite  : " << OPP << std::endl
    << "Length Adjacent  : " << ADJ << std::endl << std::endl;

  std::cout
    << "Known Trigonometric Identities (Expressed in Degrees)" << std::endl
    << "Theta:             " << angleTheta << std::endl
    << "Sine(Theta):       " << sineTheta << std::endl
    << "Cosine(Theta):     " << cosineTheta << std::endl
    << "Tangent(Theta):    " << tangentTheta << std::endl
    << "Cosecant(Theta):   " << cosecantTheta << std::endl
    << "Secant(Theta):     " << secantTheta << std::endl
    << "Cotangent(Theta):  " << cotangentTheta << std::endl << std::endl;
}

