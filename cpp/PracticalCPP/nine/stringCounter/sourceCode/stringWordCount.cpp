/*
 * stringWordCount:
 *  Is given a string/media and counts how many words are in the string.
 *
 * Author: Luis Perez
 *
 * Purpose: Introductions -_- to functions and their use. String manipulation.
 *
 * Usage: User is queued to input a string. Is then given the total amount of
 *        Words that are within the string.
 *
 * Added Funct. Letters count.
 *
 *  ** Note:
 *     A word is defined by any string, that is not interupted with a 
 *     space, underscore, or dash. Numbers are ignored in the first 
 *     implementation.
 *  ** End Note
 */
#include <iostream>
#include <string>

void runStringWordCount(void);
void stringWordCount(const std::string &input,
		     int &totalWords, int &totalLetters);
inline bool stringWordCountHelper(char inputChar);

int main(int argc, char **argv) {
  runStringWordCount();
  return(0);
}

void runStringWordCount(void) {
  std::string inputString; //String of characters to check for words.
  
  // The values to be poured into the given function, and printed out to user.. 
  int totalWords(0), totalLetters(0);
  
  std::getline(std::cin , inputString); // Place the string in inputString.
  stringWordCount(inputString, totalWords, totalLetters);

  std::cout << "Total words within the given string: " << totalWords 
	    << std::endl
	    << "Total letters within the given string: " << totalLetters 
	    << std::endl;
}

void stringWordCount(const std::string &input,
		    int &totalWords, int &totalLetters) {
  // This is more or less a shortcut for my wordcount implementation.
  // Since it is based on spaces, and things of the sort, the first word 
  // would be skipped if this is not added. Changing it at a later point.
  if(input.length() >= 1)
    totalWords++;
  
  for(unsigned int stringIndex(0); stringIndex < input.length(); ++stringIndex)
    if(stringWordCountHelper(input.at(stringIndex)))
      totalWords++; // It's a space, or other marker.
    else
      ++totalLetters; // It's just a letter.
}

inline bool stringWordCountHelper(char inputChar) {
  bool isItANewWord(false);
  
  if(inputChar == ' ' or inputChar == '-' or inputChar == '_')
    isItANewWord = true;

  return(isItANewWord);
}
