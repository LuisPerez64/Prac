//Purpose: Calculation of the students letter grades based on simple input
//Repurposed: To calculate the grade donw to a (+, , -) scale
#include <iostream>


int main(){
  int gradeInput;
  char letterGrade;
  char plusMinus(' ');//Added spec to attain the 
  std::cout << "What grade did the student attain?: " ;
  std::cin >> gradeInput;
  //Program does not ask for bounds checking, so not gonna do it...
  //but do{ }while (gradeInput <0 and gradeInput >100);

  if(gradeInput >=90)
    letterGrade = 'A';
  else if(gradeInput >=80)
    letterGrade = 'B';
  else if(gradeInput >=70)
    letterGrade = 'C';
  else if(gradeInput >=60)
    letterGrade = 'D';
  else 
    letterGrade = 'F';

  //Attain the sufix to be afixed to the notation
  gradeInput %= 10;
  if(gradeInput >7)
    plusMinus = '+';
  else if(gradeInput < 4)
    plusMinus = '-';
  //No need for the last elif point, its initiated as a ' '
  if(letterGrade == 'F')
    plusMinus = ' ';
  
  std::cout << "The letter grade for this input is " << letterGrade 
	    << plusMinus << "." << std::endl;

    return 0;
}
  
