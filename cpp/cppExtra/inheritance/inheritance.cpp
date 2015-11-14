#include <iostream>
#include <string>

class Employee{

public:
  Employee(std::string theName, float thePayRate);

  std::string getName() const;
  float getPayRate() const;

  float pay(float hoursWorked) const;

protected:
  std::string name;
  float payRate;
};


class Manager : public Employee{

public:
  Manager(std::string theName, float thePayRate, bool isSalaried);
  bool getSalaried() const;
  float pay(float hoursWorked) const;

protected:
  bool salaried;
};


Employee::Employee(std::string theName, float thePayRate){
  name = theName;
  payRate = thePayRate;
}

Manager::Manager(std::string theName, float thePayRate, bool isSalaried){
  name = theName;
  payRate = thePayRate;
  salaried = isSalaried;
}


std::string Employee::getName() const{
  return name;
}
float Employee::getPayRate() const{
  return payRate;
}

float Employee::pay(float hoursWorked) const{
  return hoursWorked * payRate;
}

bool Manager::getSalaried() const{
  return salaried;
}

float Manager::pay(float hoursWorked) const{
  if(isSalaried)
    return payRate;
  return Employee::pay(hoursWorked);
}

int main(){
  /*Employee Stan("Stan Smith", 20.00);
  Manager Steve("Steve Smith", 100000.00, false);

  std::cout << Stan.getName() << "  " << Steve.getName()
	    << Stan.getPayRate() << "  " << Steve.getName()
	    << std::endl;*/
  return 0;
}
