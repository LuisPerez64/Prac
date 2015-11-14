//Purpose: Calculation of the students letter grades based on simple input
#include <iostream>


int main(){
  int gradeInput;
  char letterGrade;

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

  std::cout << "The letter grade for this input is " << letterGrade <<"."
	    << std::endl;

    return 0;
}
  
