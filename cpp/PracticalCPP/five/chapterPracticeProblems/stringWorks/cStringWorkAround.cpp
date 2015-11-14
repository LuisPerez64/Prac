/*
 * cStringManip -- Short program to test out differences between cStrings and 
 *   Normal C++ Strings.
 *
 * Author: Luis Perez
 * 
 * Purpose: Highlight differences between the two string types.
 *
 * Usage: Minimal user interaction. Test program.
 *  More or less commenting out the cString as I test things out.
 */

#include <cstring>
#include <iostream>
#include <string>

int main(int argc, char** argv) {
  /*  char cString[50] = "Sam"; // Works. Can intiialiaze it as needed.*/
  /* 
   * char cString[50];
   * cString = "Sam"; 
   * **Does not work, yields conversion of types error.
   */
  /*
   * char cString[50];
   * std::strcpy(cString, "Sam");
   * **Works, but it really feels cumbersome, and unneeded.
   */
  /*
   * std::string cppString;
   * cppString = "Sam";
   * **Works with no hiccups, but this type of string wouldn't work for all
   * **applications. filenames and the such.
   */
  /*
   * std::string cppString = "Sam";
   * cppString = cppString.c_str();
   * **This works, of course, but the main purpose of this test is the 
   * **subsequent ones.
   */
  /*
   * std::string cppString = "Sam";
   * char cString[50] = cppString;
   * **This does not work, as cppString is not a cString...
   */
  /*
   * std::string cppString = "Sam";
   * char cString[50] = cppString.c_str();
   * **This still does not work, guess have to do string copy instead.
   */
  /*
   * std::string cppString = "Sam";
   * char cString[50];
   * std::strcpy(cString, cppString);
   * **This does not work, because of cppString not being a cString as needed.
   */
  /*
   * std::string cppString = "Sam";
   * char cString[50];
   * std::strcpy(cString, cppString.c_str());
   * **This of course works since it converts the cppString into a cString 
   * **before attempting to copy it over into the cString "object" that we are
   * **currently working with. This is expected, but weird in itself.
   */
  /*
   * char cString[50]= "Sam";
   * std::string cppString = cString;
   * **This works, of course again since cppStrings inheritted string 
   * **string manipulation. The lesson overall. Only use cStrings when needed,
   * **go forth with the knowledge that should you need them, you can convert
   * **cppStrings into cStrings with ease, and go from there.
   */

  std::string cppString = "Sam";
  char cString[50] = "Sam";

  /*
   * cppString += " I Am"; == std::strcat(cString, " I Am");
   * **Honestly which one would you normally like to use...
   */

  std::cout << cppString << std::endl;
}
