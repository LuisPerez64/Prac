//Purpose: Pretax pay calculator. Will attempt to add formal pay points to this
//Later on.

#include <iostream>
#include <iomanip>
int main(){
 
  float payRate;//The payrate before overtime included for employee
  float overTime;//Total overtime done
  float overTimePayRate;//The payrate * 1.5 for ime and a half
  float overTimePay; //The total paid to the employee in OVertime
  float grossPay; //The total paid before taxes to the employee.
  int hours;//total hours worked by the employee

  std::cout << "How much do you get paid per hour?: ";
  std::cin >> payRate;

  std::cout << "Alright, and how many hours did you work this"
	    << " pay period?: ";
  std::cin >> hours;

  if(hours <= 40)
    grossPay = payRate * hours;
  else if(hours > 40){//Calculate the overtime Pay for the Employee
    overTime = hours - 40;
    overTimePayRate = payRate * 1.5; 
    overTimePay = overTime * overTimePayRate;
    grossPay = payRate * 40;//Base case overtime is deducted 40 hours min.
  }

  grossPay += overTimePay;//adjusts for overtime pay, if there was any
  std::cout << std::fixed;
  std::cout << std::setprecision(2)
	    << "The total pay for this employe working " << hours << " hours"
	    << std::endl << "is $" << grossPay << " dollars." << std::endl; 

  return 0;
}
