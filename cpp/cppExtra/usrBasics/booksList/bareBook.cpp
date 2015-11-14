#include <iostream>
#include <fstream>
#include <string>

// This whole thing is insanely ineficient... Not bad for this size, but damn..
bool isAuthor(std::string);
std::string authorName(std::string);


int main() { 
  std::ifstream inputFile;
  inputFile.open ("Book List.txt");
  if (!inputFile.is_open())
    std::cout << "This ain't it";

  std::string inputLine;
 
  while (inputFile.good()) {
  std::getline(inputFile, inputLine);
  if(isAuthor(inputLine)) {
    std::cout << authorName(inputLine) << std::endl;
    }else {
    std::cout << inputLine << std::endl;
    }   
  }
  inputFile.close();

  return(0);
}


bool isAuthor(std::string input) {
  bool isIt(false);
  
  if(input.find(": #") != std::string::npos)
    isIt = true;
      
  return(isIt);
}

std::string authorName(std::string input) {
  return(input.substr(0, input.find(':')));
}
