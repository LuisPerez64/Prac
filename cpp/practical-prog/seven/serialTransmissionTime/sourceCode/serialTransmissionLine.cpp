/*
 * serialtransmissionTimeCalculator --
 *   takes in user input and produces to the user the amount of time it would
 *   take to send that amount of data through a serial transmission line.
 *
 * Author: Luis Perez
 * Purpose: Self Use and Practice in preplanning
 *
 * usage:
 *   Ask user for input of the serial transmission unit speed
 *   Ask user for the size of the file to be sent, in MB
 *   Output to the user the time, in different time intervals, of the process
 */

#include <iostream>
#include "serialTransmissionLine.hpp"

int main(int argc, char* argv[]) {
  //Nothing to be initialized, not looping no need.
  runSerialTransmissionCalculator();

  return(0);
}

/** Functions that have been tested and work **/
void runSerialTransmissionCalculator(void) {
  timeUnits outputTimeUnits; // Times that are going to be output to the user.
  timeUnits hardwiredTimes; // Times to be used in the calculations
  unsigned long int sizeOfFileInMB(0);
  unsigned int transmissionSpeedInBytesPerSecs(0);
  unsigned int secondsToTransferFile;

  assignNeededTimes(hardwiredTimes); // Assign the seconds intervals

  std::cout << "How many bytes per second are transmitted: ";
  std::cin >> transmissionSpeedInBytesPerSecs;
  std::cout << "How many Megabytes are being transmitted: ";
  std::cin >> sizeOfFileInMB;
  // Convert MB's into bytes (MB * 1024^2)
  unsigned int sizeOfFileInBytes(sizeOfFileInMB * 1024 * 1024);

  secondsToTransferFile = sizeOfFileInBytes / transmissionSpeedInBytesPerSecs;

  assignOutputTimes(secondsToTransferFile, outputTimeUnits, hardwiredTimes);
  displayOutputTimes(outputTimeUnits);
  std::cout << std::endl
	    << "For " << sizeOfFileInMB << " Megabytes at "
	    << transmissionSpeedInBytesPerSecs << " bytes per second."
	    << std::endl;
}

void  displayOutputTimes(const timeUnits &outputTimeUnits) {
  std::cout << std::endl
	    << "The total amount of time needed to transfer the data:"
	    << std::endl;
  // Can't use a switch because of the multivariable check...
  if(outputTimeUnits.years > 0)
    std::cout << "Years: " << outputTimeUnits.years << std::endl;
  if(outputTimeUnits.months >0)
    std::cout << "Months: " << outputTimeUnits.months << std::endl;
  if(outputTimeUnits.weeks > 0)
    std::cout << "Weeks: " << outputTimeUnits.weeks << std::endl;
  if(outputTimeUnits.days > 0)
    std::cout << "Days: " << outputTimeUnits.days << std::endl;
  if(outputTimeUnits.hours > 0)
    std::cout << "Hours: " << outputTimeUnits.hours << std::endl;
  if(outputTimeUnits.minutes > 0)
    std::cout << "Minutes: " << outputTimeUnits.minutes << std::endl;
  if(outputTimeUnits.seconds > 0)
    std::cout << "Seconds: " << outputTimeUnits.seconds << std::endl;
}
void assignOutputTimes(int secsNeededToTransferFile,
		       timeUnits &outputSeconds, const timeUnits &secondsInA) {
  /*
    Basic calculation process
    Attain the amount of -given interval value- in the secs provided
    then remove that value from the total operation, to get the smaller
      interval that is going to be calculated.
   */

  // Attain the total years from calculation
  outputSeconds.years =
    assignOutputHelper(secsNeededToTransferFile, secondsInA.years);
  secsNeededToTransferFile -= (outputSeconds.years * secondsInA.years);

  // Attain the total months from calculation
  outputSeconds.months =
    assignOutputHelper(secsNeededToTransferFile, secondsInA.months);
  secsNeededToTransferFile -= (outputSeconds.months * secondsInA.months);

  // Attain the total weeks from calculation
  outputSeconds.weeks =
    assignOutputHelper(secsNeededToTransferFile, secondsInA.weeks);
  secsNeededToTransferFile -= (outputSeconds.weeks * secondsInA.weeks);

  // Attain the total days from calculation
  outputSeconds.days =
    assignOutputHelper(secsNeededToTransferFile, secondsInA.days);
  secsNeededToTransferFile -= (outputSeconds.days * secondsInA.days);

  // Attain the total hours from calculation
  outputSeconds.hours =
    assignOutputHelper(secsNeededToTransferFile, secondsInA.hours);
  secsNeededToTransferFile -= (outputSeconds.hours * secondsInA.hours);

  // Attain the total Minutes from calculation
  outputSeconds.minutes =
    assignOutputHelper(secsNeededToTransferFile, secondsInA.minutes);
  secsNeededToTransferFile -= (outputSeconds.minutes * secondsInA.minutes);

  // Attain the total Seconds left over from calculation
  outputSeconds.seconds = secsNeededToTransferFile;
}

int assignOutputHelper(int secondsForOps, const int &secondsInA) {
  int returnValue(0);
  /*
   * return = 500 seconds / 60 seconds in a minute
   */
  // Take the seconds that are given and divide them by the measured seconds
  // in the needed interval from the calculation.
  returnValue = secondsForOps / secondsInA;
  return(returnValue);
}

void assignNeededTimes(timeUnits &input) {
  input.seconds = 1; // 1 second in a second
  input.minutes = 60 * input.seconds; // 60 seconds in a minute
  input.hours = 60 * input.minutes; // 60 minutes in an hour
  input.days = 24 * input.hours; // 24 hours in a day
  input.weeks = 7 * input.days; // 7 days in a week

  // Breaks down here, these measurements are too far off for accuracy
  // at the interval points that are stated above.
  input.months = 30.4 * input.days; // 30.4 days in a month, cast to an int
  input.years = 365 * input.days; // 365 days in a year, leaps not inclusive

  // Test for the amount of seconds in each interval
  /*
     std::cout << "minute: " << input.minutes  << std::endl
     << "hour: " << input.hours << std::endl
     << "Day: " << input.days << std::endl
     << "Week: " << input.weeks << std::endl
     << "Month: " << input.months << std::endl
     << "Year: " << input.years << std::endl;
  */
}
