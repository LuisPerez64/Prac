// C Libraries first ~ Inherent Libraries ~ My Libraries 
#include <ctime> // std::time 
#include <cstdlib> // std::srand | rand 
#include <iostream> // std::cout | std::cin 
#include <vector> // std::vector<T> | std::vector<T>::iterator
#include <algorithm> // std::algorithm::scramble
#include <string> // std::string | 
#include <fstream> // Not implemented yet.
#include <sstream> // std::stringstream | .str()

// Test function imported, just converts integers into a formatted string
// Used within the function inputStrings
std::string makeMeAString(int);

void scrambleData(std::vector<int> &a);
std::vector<std::string> inputStrings(std::vector<int> &a);
void outputStrings(std::vector<std::string> &a);

int main(int argc, char* argv[]) {
  std::vector<int> scrambledVectorOfInts;
  scrambleData(scrambledVectorOfInts); //Scramble the Data.

  std::vector<std::string> scrambledQuestions
    (inputStrings(scrambledVectorOfInts)); // Pluck the questions from the file

  outputStrings(scrambledQuestions); // Output the questions to the screen.

  return(0);
}

// Inefficient manner of makig the scrambled vector. Can theoretically run forever
void scrambleData(std::vector<int> &inputVector) {
  int inputCounter;
  int randInput;
  std::vector<int>::iterator inputIter(inputVector.begin()); // Iterator for ^^

  std::srand(std::time(NULL)); // Make the number more 'random' seed with time

  std::cout << "How many questions are going to be a part of this quiz?: ";
  std::cin >> inputCounter;

  // There has to be a more efficient way of doing this...
  for (int tempCounter(inputCounter);
       inputCounter != 0;
       /* Blank on Purpose*/) {
    randInput = (rand() % tempCounter) + 1;
    inputIter = find (inputVector.begin(),
		      inputVector.end(),
		      randInput);

    // Checks if the value passed in is within the given vector, no duplicates.
    if (inputIter == inputVector.end()) {
      --inputCounter;
      inputVector.push_back(randInput);
    }
  }
}

/*
  Read points from a file, evaluating if its a new question or a continued one
  Take that input, and convert it into the string that it needs to be 
  based on the number that is before the question.
  In essence, read the input file, match the numbers to the number at the
  vector point, push them into a vector that will hold said string,
  using possibly getline until a line with the format string 
  number. is met again, or format is met.
  This will be using the Regex library, which I have yet to even breach
*/

// Does nothing as of yet. Works with the testingLibrary though
std::vector<std::string> inputStrings(std::vector<int> &inputVector) {
  std::vector<std::string> stubReturn;
  int counter(0);
  while (true) {
    if (counter >= inputVector.size())
      break;
    stubReturn.push_back(makeMeAString(inputVector.at(counter)));
    ++counter;
  }
  return stubReturn;
}

// This guy works as he should. Outputs the strings that are in the vector
// Handed to it.
void outputStrings(std::vector<std::string> &inputVector) {
  std::cout << "The scrambled quiz questions are: " << std::endl;
  int totalQuestions((signed)inputVector.size() - 1);
  
  while (true) { 
    if (totalQuestions < 0)
      break;
    std::cout << inputVector.at(totalQuestions) << std::endl;
    --totalQuestions;      
  }

  /*
  inputIter = inputVector.begin();
  while (inputIter != inputVector.end()) {
    std::cout << *inputIter <<std::endl;
    ++inputIter;
  }
  */
  std::cout << std::endl;
}



//Test 
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
  } else
    outputString << "Not a number in my range";
  
  // This is what is appended to every thing forthcoming.
  return (outputString.str());
}
