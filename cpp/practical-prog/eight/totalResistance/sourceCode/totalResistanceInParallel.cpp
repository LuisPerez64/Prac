/*
 * totalResistanceInParallel--
 *   Is fed a series of resistor values(ints, for now), and returns their 
 *   total resistance in parallel
 *
 * Author: Luis Perez
 *
 * Purpose: Continued practice in the point of new conditionals/loops. Applying
 *  basic mathematical formulas to some diverse points.
 *
 * Usage: User inputs resistor values, until they are satisfied, and input 0 
 *  when they are done inputing the resistor values. Program then outputs the 
 *  total value of the resistors if they were to be wired in parallel.
 */

#include <iostream> // std::cout | std::cin | std::fixed
#include <iomanip> // std::setprecision;

typedef struct resistorInParallel{
  int numerator;
  int denominator;
} rIP;

void runTotalResistanceCalculator(void);
rIP getUpdatedResistor(rIP newResistor,rIP resistorSoFar);
void printOutResistor(const rIP &inputResistor);
int bruteForceLCM(int firstDivisor, int secondDivisor);

int main() {
  runTotalResistanceCalculator();

  return(0);
}


void runTotalResistanceCalculator(void) {
  // The returned resistance ~ 1/R= 1/R(0) +...+ 1/R(n) ~> R/n = R/1
  float totalResistanceInParallel(0.0);
  // the resistors that are to be used in the program.
  rIP newResistor, resistorSoFar;
  // Toggle checks if first resistor is being input, branches to new if not.
  bool toggle(false);
  // The new resistor value to be put in by user.
  int resistance(1); 
  std::cout << "Welcome to the parallel resistance calculator." << std::endl;
  std::cout 
    << "Begin inputting values to calculate running resistance in parallel." 
    << std::endl;
  
  while(true) {
    std::cout << "Input Value: ";
    std::cin >> resistance;
    
    if(resistance == 0)
      break;
    if(resistance < 0) {
      std::cout << "Sorry no such thing as a negative resistor. ";
      continue;
    }
      
    if(toggle) {
      newResistor.numerator = 1;
      newResistor.denominator = resistance;
      resistorSoFar = getUpdatedResistor(newResistor, resistorSoFar);
    } else { // This is run only once, and is a case for when only one input.
      resistorSoFar.numerator = 1;
      resistorSoFar.denominator = resistance;
      toggle = true;
    }
    
    // cast the points as floats, to attain a floating point number result.
    totalResistanceInParallel =
      ((float)resistorSoFar.denominator / (float)resistorSoFar.numerator);
    
    // Outputs the total resistance in parallel as the user inputs values.
    std::cout
      << std::fixed << std::setprecision(4) 
      << "The resistance in parallel so far: " 
      << totalResistanceInParallel << " Ohms." << std::endl;   
  }
  
}


/*******************Tested*******************/
rIP getUpdatedResistor(rIP newResistor, rIP resistorSoFar) {
  rIP returnedResistor; // resistor to be returned to the caller.
  int leastCommonMultiple // used for the common denominator.
    (bruteForceLCM(newResistor.denominator, resistorSoFar.denominator));
 
  // Update the newResistors Values.
  int multiplyBy = leastCommonMultiple / newResistor.denominator;
  newResistor.numerator *= multiplyBy;
  newResistor.denominator = leastCommonMultiple;
  
  // Update the resistorSoFars Values.
  multiplyBy = leastCommonMultiple / resistorSoFar.denominator;
  resistorSoFar.numerator *= multiplyBy;
  resistorSoFar.denominator = leastCommonMultiple;
 
  // Update the returnedResistor
  // Updated values within the resistor 1/12 + 1/12 = 2/12
  returnedResistor.numerator = newResistor.numerator + resistorSoFar.numerator;
  returnedResistor.denominator = leastCommonMultiple;
  /*
    std::cout << "New Resistor: " << std::endl;
    printOutResistor(newResistor);

    std::cout << "Resistor So Far: " << std::endl;
    printOutResistor(resistorSoFar);

    std::cout << "Resistor To Be Returned: " << std::endl;
    printOutResistor(returnedResistor);
  */
  return(returnedResistor);
}

int bruteForceLCM(int firstDivisor, int secondDivisor) {
  // Goes through the total numbers, and in a brute force manner, algorithmic
  // involes primes, goes through the numbesr until a number is met that both
  // divide evenly remaining with 0;
  for(int moduloIndex(firstDivisor);/* */; ++moduloIndex) 
    if((moduloIndex % firstDivisor == 0) and 
       (moduloIndex % secondDivisor == 0))
      return(moduloIndex); // Once this number is met return it.
}

void printOutResistor(const rIP &inputResistor) {
  std::cout // prints out the numerator and the denominator ogf the given 
    //resistor. Mainly used to test the values in them at the given time.
    << "Numerator: " << inputResistor.numerator 
    << std::endl 
    << "Denominator: " << inputResistor.denominator 
    << std::endl;
}

