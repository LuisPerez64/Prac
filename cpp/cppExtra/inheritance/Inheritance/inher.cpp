#include <iostream>
#include <string>
#include "inher.hpp"

using namespace std;

Employee::Employee(string theName, float thePayRate)
{
  name = theName;
  payRate = thePayRate;
}

string Employee::getName() const
{
  return name;
}

float Employee::getPayRate() const
{
  return payRate;
}

float Employee::pay(float hoursWorked) const
{
  return hoursWorked * payRate;
}


Manager::Manager(string theName,
                 float thePayRate,
                 bool isSalaried)
  : Employee(theName, thePayRate)
{
  salaried = isSalaried;
}

bool Manager::getSalaried() const
{
  return salaried;
}

float Manager::pay(float hoursWorked) const
{
  if (salaried)
    return payRate;
  /* else */
  return Employee::pay(hoursWorked);
}

int main(){
  Employee Stan("Stan Smith", 20.00);
  Manager Steve("Steve Smith", 100000.00, false);

  std::cout << Stan.getName() << "  " << Steve.getName()
	    << Stan.getPayRate() << "  " << Steve.getName()
	    << std::endl;
  return 0;
}

