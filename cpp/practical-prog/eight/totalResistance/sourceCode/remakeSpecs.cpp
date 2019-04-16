#include <iostream>

struct resistorInParallel{
  int numerator;
  int denominator;
};
typedef struct resistorInParallel rIP;

void runTotalResistanceCalculator(void);
void findLeastCommonDenominator(rIP &first, rIP &second);
void printOutResistor(const rIP &resistor);
int bruteForceLCD(int firstDivisor, int secondDivisor);
int bruteForceGCM(int numerator, int denominator);
rIP getTotalParallelResistance(rIP &firstResistor, rIP &secondResistor);

void test(void);
int main() {
  //  test();
  runTotalResistanceCalculator(); 
}

void test(void) {
  int divisor, divisorTwo;
  
  while(true) {
    std::cin >> divisor >> divisorTwo;
    std::cout << bruteForceLCD(divisor, divisorTwo) << std::endl;
  }
  
}
void runTotalResistanceCalculator(void) {
  float totalResistanceInParallel(0.0);
  rIP newResistor, resistorSoFar;
  bool toggle(false);
  int resistance(0);

  while(true) {
    std::cin >> resistance;
    if(resistance == 0)
      break;

    if(toggle) {
      newResistor.numerator = 1;
      newResistor.denominator = resistance;
      resistorSoFar = getTotalParallelResistance(newResistor, resistorSoFar);
    } else { // This is run only once, and is a case for when only one input. 
      resistorSoFar.numerator = 1;
      resistorSoFar.denominator = resistance;
      toggle = true;
    }
    std::cout << "Resistor so Far: ";
    printOutResistor(resistorSoFar);
    totalResistanceInParallel =
      (float)resistorSoFar.denominator / (float)resistorSoFar.numerator;
    std::cout << "Total Resistance: " << totalResistanceInParallel 
	      << std::endl;
  }

}

rIP getTotalParallelResistance(rIP &firstResistor, rIP &secondResistor) {
  rIP returnedResistor;
 
  // Find the least common denominator amongst the two resistor values.
  findLeastCommonDenominator(firstResistor, secondResistor);

  { // Its own block.
    returnedResistor.numerator = 
      firstResistor.numerator + secondResistor.numerator;
    returnedResistor.denominator = firstResistor.denominator;
  }
  
  // This causes the value to be as small as possible.
  int divideBothBy
    (bruteForceGCM(returnedResistor.numerator, returnedResistor.denominator));
  returnedResistor.numerator /= divideBothBy;
  returnedResistor.denominator /= divideBothBy;
  
  printOutResistor(returnedResistor);
  printOutResistor(firstResistor);
  printOutResistor(secondResistor);

  return(returnedResistor);
}

/* Work May Need More testing */
void findLeastCommonDenominator(rIP &first, rIP &second) {
  // Makes it so that first is always the higher of the two resistor values.
  if(second.denominator > first.denominator) {
    int temp(first.denominator);
    first.denominator = second.denominator;
    second.denominator = temp;
  }

  // If they are modularly divisible then the basic bring it up to par works.
  if(first.denominator % second.denominator == 0) {
    int multiplyNumeratorBy(first.denominator / second.denominator);
    second.numerator *= multiplyNumeratorBy;
    second.denominator = first.denominator;
  } else {
  int leastCommonDenom(bruteForceLCD(first.denominator, second.denominator));
 
  // Attains the value to multiply the numerators by, to keep the fractions
  // achieving the same decimal number value.
  int multiplyFirstNumerator(leastCommonDenom / first.denominator);
  int multiplySecondNumerator(leastCommonDenom / second.denominator);
  
  // make the divisors the same;
  first.denominator = second.denominator = leastCommonDenom;
 
  // Multiply them by them by respective points. Normalizing the fractions.
  first.numerator *= multiplyFirstNumerator;
  second.numerator *= multiplySecondNumerator;
  }
}

int bruteForceGCM(int first, int second) {
  int returnValue(1);
  for(int moduloIndex(2); moduloIndex <= first; ++moduloIndex)
    if(first % moduloIndex == 0 and second % moduloIndex == 0) {
      returnValue *= moduloIndex;
      first /= moduloIndex;
      second /= moduloIndex;
      moduloIndex = 1; // Number is incremented to two after for loop.
    }
  return(returnValue);
}

int bruteForceLCD(int firstDivisor, int secondDivisor) {
  // Starts the modulo operations from the first Divisor to attain their least
  // common denominator.

  for(int moduloIndex(2);/* Blank */; ++moduloIndex) 
    if((moduloIndex % firstDivisor == 0) && (moduloIndex % secondDivisor == 0))
      return moduloIndex;
}
  
void printOutResistor(const rIP &resistor) {
  std::cout << "Numerator: " << resistor.numerator << "  "
	    << "Divisor: " << resistor.denominator << std::endl;
}
