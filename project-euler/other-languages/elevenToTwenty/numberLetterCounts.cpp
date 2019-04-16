#include <iostream>
#include <string>
#include <sstream>

std::string makeMeAString(int);
inline int findMyValue(std::string);

int main(int argc, char *argv[]) {
  int total(0);

  for (int index(1); index <= 1000; ++index) {
    std::string inputString(makeMeAString(index));
    total += findMyValue(inputString);
  }

  std::cout << "Total of all the letters used to make the 1000 numbers is: "
	    << total << "." << std::endl; 
    
  return(0);
}

//Everything is handled through cascading recursion. 
// Try and do it with the return of a string, after making sure this way works.
std::string makeMeAString(int input) {
  std::stringstream outputString;
  
  if (input <= 19)
    switch(input) {
    case 1:
      outputString << "one";
      break;
    case 2:
      outputString << "two";
      break;
    case 3:
      outputString << "three";
      break;
    case 4:
      outputString << "four";
      break;
    case 5:
      outputString << "five";
      break;
    case 6:
      outputString << "six";
      break;
    case 7:
      outputString << "seven";
      break;
    case 8:
      outputString << "eight";
      break;
    case 9:
      outputString << "nine";
      break;
    case 10:
      outputString << "ten";
      break;
    case 11:
      outputString << "eleven";
      break;
    case 12:
      outputString << "twelve";
      break;
    case 13:
      outputString << "thirteen";
      break;
    case 14:
      outputString << "fourteen";
      break;
    case 15:
      outputString << "fifteen";
      break;
    case 16: 
      outputString << "sixteen";
      break;
    case 17:
      outputString << "seventeen";
      break;
    case 18:
      outputString << "eighteen";
      break;
    case 19:
      outputString << "nineteen";
      break;
    }
  else if (input <= 99) {
    int temp(input - (input % 10));
    switch(temp) {
    case 20:
      outputString << "twenty";
      break;
    case 30:
      outputString << "thirty";
      break;
    case 40:
      outputString << "forty";
      break;
    case 50:
      outputString << "fifty";
      break;
    case 60: 
      outputString << "sixty";
      break;
    case 70:
      outputString << "seventy";
      break;
    case 80:
      outputString << "eighty";
      break;
    case 90:
      outputString << "ninety";
      break;
    }

    if (input % 10 != 0) // Returns 1 - 10
      outputString << '-' << makeMeAString(input % 10);

  } else if (input <= 999) {
    int temp((input - (input % 100)) / 100); // Make it a one digit number
    
    outputString << makeMeAString (temp) <<' ' <<  "hundred"; // Returns 1-9
    
    if (input % 100 != 0)  // Attain the rest of the input if not an even 100
      outputString << " and " << makeMeAString(input % 100); // Returns 10-99

  } else if (input <= 9999) {
    int temp ((input - (input % 1000)) / 1000); // Same as above
    outputString << makeMeAString (temp) << ' ' << "thousand"; // returns 1-9
    
    if (input % 1000 != 0)
      outputString << ' ' << makeMeAString(input % 1000); // Returns 100-999
  }
  
  // This is what is appended to every thing forthcoming.
  return (outputString.str());
}

// Doing this the hard way, in order to keep coherence in the english spellings.
inline int findMyValue(std::string input) {
  int total(0);
  for (;input.length() != 0; input.erase(0, 1))
    if (input.at(0) != '-' and input.at(0) != ' ') 
      ++total;
    
  return(total);
}
