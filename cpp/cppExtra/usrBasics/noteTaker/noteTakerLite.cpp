#include <iostream>
#include <fstream>
#include <string>

/*
 Basic isOpen function to make sure things are not overwritten.
 */
inline bool fileExists(const char* filename);
inline void clearBuffer(void);
inline void createHeader(std::ofstream &outputFile, const std::string &name);

int main(int argc, char **argv) {
  std::string fileName;
  std::ofstream outputFile; // File to hold everything in place.

  std::cout << "Name of the file that you would like to write to?: ";
  std::getline(std::cin, fileName);
  std::string tempFileName(fileName);
  fileName += ".txt"; // Append the .txt filetype to the file in question.

  if(fileExists(fileName.c_str())) {
    outputFile.open(fileName.c_str(), std::ofstream::app | std::ofstream::out);
    std::cout << "Opened to append" << std::endl;
  } else {
    outputFile.open(fileName.c_str(), std::ofstream::trunc|std::ofstream::out);
    createHeader(outputFile, tempFileName);
  }

  outputFile.close();
  return(0);
}


inline bool fileExists(const char* filename) {
  std::ifstream inputFile(filename);
  bool result(true);
  
  if(!inputFile.is_open())
    result = false;
  
  inputFile.close();
  return(result);
}

inline void createHeader(std::ofstream &outputFile, const std::string &fName) {
  outputFile << "Tutorial Name is: " << fName << std::endl << std::endl;
}

inline void clearBuffer(void) {
  int c ='\0';
  while((c != '\n')  and (c != EOF))
    c = std::cin.get();
}   
