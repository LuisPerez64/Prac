//Purpose: Conversion of Clesius to farenheit, Nothing More Nothing Less
#include <iostream>		//cout | cin | endl


int main (){

  float celsius;  //Container to hold user input for celsius to be converted
  float farenheit; //Container for the result of the conversion
  
  std::cout << "How many degress Celsius are you converting?: ";
  std::cin >> celsius;
  
  farenheit = (9.0/5.0) * celsius + 32.0;
  
  std::cout << "That equates to about " << farenheit << " degrees farenheit"
	    << std::endl;

  return 0;
}
