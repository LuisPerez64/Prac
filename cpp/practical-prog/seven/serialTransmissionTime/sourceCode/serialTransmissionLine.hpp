#ifndef SERIAL_TRANS_CALC
#define SERIAL_TRANS_CALC
// Header definition for the serialTransmission program


struct timeUnits { // Can't use newer C++ initialization points, no Classes
  int years;
  int months;
  int weeks;
  int days;
  int hours;
  int minutes;
  int seconds;
};
// Runs in main , the actual program that is beind done
void runSerialTransmissionCalculator(void);

// Gives the counter for the amount of seconds that are within
// Each of the given intervals, 60 in a minute ....
void assignNeededTimes(timeUnits &input);

/*
 * Assigns the amount of years, months ... seconds that take place
 * in the amount of seconds that it takes to process the data
 */
void assignOutputTimes(int secondsNeededToTransferFile,
		       timeUnits &outputSeconds, const timeUnits &secondsInA);
/*
 * helper function for the above, does the basic calculation to attain
 * the amount of times that the interval takes in
 * is given the full seconds that are left in the processing
 * also takes in the amount of seconds that are within that interval
 */
int assignOutputHelper(int secondsForOps, const int &secondsInA);
/*
 * Basic function to display all of the given interval units to the user
 */
void  displayOutputTimes(const timeUnits &outputTimeUnits);

#endif // SERIAL_TRANS_CALC
