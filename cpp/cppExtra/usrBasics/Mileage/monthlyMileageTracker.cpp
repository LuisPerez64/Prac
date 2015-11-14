#include <iostream> // std::cout | std::cin
#include <fstream> // std::fstream
#include <string> // std::string
#include <cstdlib> // atoi

void createHeader(std::ofstream &inputFile, std::string date);
void fileManip(std::ofstream &inputFile);
void clearBuffer();
// Input reading probems are happening right now. Have to fix all of those as soon as possible, but not irght nows........... FUCKING GETLINE

/*Inefficient as all hell but this should work for the purpose being placed.*/
int main(int argc, char *argv[]) {
  std::string month; // To be used for the placement of the files name
  std::cout << "What month are you inputting into?: ";
  std::cin >> month;
  std::string tempMonth(month); // Made prior to making the str a .txt file.
  month += ".txt"; // Append the word txt to make the month a text file.

  std::ofstream outputFile; // Place holder for the output file stream 
  std::ifstream checkMe(month.c_str()); // Simply to make the fileOpen? test.
  if (checkMe.is_open()) { // If the file is open then append to it
    outputFile.open(month.c_str(), std::ofstream::app);
  }else { // Else make a full new file, and create the header for it.
    outputFile.open(month.c_str(), std::ofstream::out);
    createHeader(outputFile , tempMonth); 
  }
  
  fileManip(outputFile);
  return(0);
}


void fileManip(std::ofstream &outputFile) {
  std::string date;
  char answer;
  bool multipleDays(false);
  
  std::cout << "Will this be a multiple work day update(y/n): ";
  std::cin >> answer;
  clearBuffer();   
  if(answer == 'y' || answer == 'Y') {
    multipleDays = true;
    std::cout << "To break out of the date input process input ~~"<<std::endl;
  }

  do{
    std::cout << "Date of mileage point ~ (Format 'Month-Day-Year'): ";
    std::getline (std::cin, date);
    if(date.at(0) == '~')
      break;

    outputFile << date << ":" << std::endl ;    
    float miles;
    std::string locations;
    while(true) {
      std::cout << "Miles: ";
      std::cin >> miles;
      std::cout << "Locations Traveled, press enter when done input:" 
		<<std::endl
		<< "Seperate locations with commas" << std::endl;
      clearBuffer();
      std::getline(std::cin , locations);

      outputFile << "\t" << miles << " Miles traveled." 
		 << std::endl << "\tPlaces Traveled: " 
		 << std::endl << "\t  " << locations << std::endl << std::endl;

      std::cout << "Would you like to put in more locations for this" 
		<< "day (y/n)?: ";
      std::cin >> answer;
      if(answer == 'n' || answer == 'N')
	break;
      clearBuffer();
    }    
  }while(multipleDays);
}


// Can make this better in the long run, doesn't really matter much...
void createHeader(std::ofstream &inputFile, std::string date) {
  inputFile << date << " Mileage Points"  
	    << std::endl;
}

void clearBuffer() {
  while (std::cin.get() != '\n')
    std::cin.get();
}
