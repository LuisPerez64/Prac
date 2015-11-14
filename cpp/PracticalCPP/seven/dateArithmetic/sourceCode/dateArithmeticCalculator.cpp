/*
 * DateArithmeticCalculator--
 *    Calculates the amount of days between two given days
 *
 * Author: Luis Perez
 * Purpose: More or less training in basic programming process, and preplanning
 *
 * Usage:
 *   Prompts user to input two dates mm/dd/yyyy and then outputs the amount of
 *   days that have passed in between those two given dates.
 */

#include <iostream>
#include "dateArithmeticCalculator.hpp"

int main(int argc, char* argv[]) {
  // No loop needed at the time.
  runDateArith();

  return(0);
}

void runDateArith(void) {
  date startDate; // Structs created above to hold the given data cleanly.
  date endDate;
  int totalDays(0); // The days between the two dates, the accumulator.
  
  std::cout << "Start Date (input format (mm dd yyyy)): ";
  std::cin >> startDate.month >> startDate.day >> startDate.year;
  std::cout << "Ending Date (input format (mm dd yyyy)): ";
  std::cin >> endDate.month >> endDate.day >> endDate.year;
  
  // Get the days that are left in the given month,
  // if the years are not exactly the same;
  if(startDate.year != endDate.year)
    totalDays += getDaysLeftInYear(startDate, endDate);
  else
    totalDays += daysSpanInYear(startDate, endDate);

  std::cout << "There are " << totalDays << " Days between the dates: " 
	    << startDate.month << "-" << startDate.day << "-" 
	    << startDate.year << " and " 
	    << endDate.month << "-" << endDate.day << "-" << endDate.year 
	    << std::endl << "End dates inclusive." << std::endl << std::endl;
  return;
}


/** Testing Function may be good, but not too sure as of yet.**/
int getDaysLeftInYear(const date &start, const date &end) {
  int daysFromStartDate(0);
  int daysUpToEndDate(0);
  int totalDays(0);
 
  // Attain the days left in the year from the input day til 12/31/....
  for(int temp(12); temp > start.month; --temp)
    daysFromStartDate += daysInMonth(temp, start.year);
  int tempCounter(start.day);
  tempCounter = daysInMonth(start.day, start.year) - tempCounter;
  daysFromStartDate += tempCounter;  

  /* Test */ 
  //  std::cout << "Test: " << daysFromStartDate << " Should be 365" << std::endl;

  // Attain the days up to, and including the last day in the end date point
  for(int temp(1); temp < end.month; ++temp) 
    daysUpToEndDate += daysInMonth(temp, end.year);
  daysUpToEndDate += end.day;

  /* Test */
  //  std::cout << "Test: " << daysUpToEndDate << " Should be 366" << std::endl;
 
  // Take out the dates that have already been calculated before.
  for(int startTemp(start.year + 1), endTemp(end.year - 1);
      startTemp <= endTemp; ++startTemp) {
    if(isLeapYear(startTemp))
      totalDays += 366;
    else 
      totalDays += 365;
  }

  /* Test */
  // std::cout << "Total Days between the years: " << totalDays;

  totalDays += daysUpToEndDate +  daysFromStartDate;
  return(totalDays);
}


/***************** Work as they should **********************/
int daysSpanInYear(const date &startDate, const date &endDate) {
  int totalDays(0);
  
  // If the given points are the same month then just subtract end from start.
  if(startDate.month == endDate.month)
    totalDays = (endDate.day - startDate.day);
  else {
    totalDays += endDate.day; // Add in the days at the end
    totalDays += // Add in the days from the first month
      (daysInMonth(startDate.month, startDate.year)) - startDate.day; 
    int temp(startDate.month + 1); // Used to exclude the initial month. 
    while(temp < endDate.month) { // Get the total days from the months.
      totalDays += daysInMonth(temp, startDate.year);
      ++temp;
    }
  }  
  
  return(totalDays + 1); // Inclusive of the last day.
}

bool isLeapYear(const int &inputYear) {
  bool result(false);
  
  if(inputYear % 4 == 0 and ((inputYear % 100 != 0) or (inputYear % 400 == 0)))
    result = true;

  return(result);
}


int daysInMonth(int monthInQuestion, int yearInQuestion) {
  int howManyDays(0);
  
  if(monthInQuestion == 4 || monthInQuestion == 6 || monthInQuestion == 9 ||
     monthInQuestion == 11) {
    howManyDays = 30;
  }else if(monthInQuestion == 2){
    if(isLeapYear(yearInQuestion))
      howManyDays = 29;
    else
      howManyDays = 28;
  }else 
    howManyDays = 31;

  return(howManyDays);
}
