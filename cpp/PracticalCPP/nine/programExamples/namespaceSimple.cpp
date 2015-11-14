#include <iostream>
/*
 * namespaceSimple
 *  Comment practice program. Run is not interactive.
 *
 * Author: Luis Perez
 *
 * Purpose: Comment in the points that I feel need to be highlighted in the 
 *  form of comment heavy-ish syntax, to attain a bit more familiarization with
 *  namespaces and things of the sort that are directly involved in the making.
 *
 * Usage: No Interaction. Just prints out the given data.
 */


/*
  In my view point, which is undoubtedly wrong. Namespaces work as structs, 
  sort of, the functions that are declared within this namespace can be 
  accessed from outside of it, with no problems, but you have to tell them 
  where they are coming from, or things start to get out of hand a bit, and 
  they then do not want to work.

  Counterpoint. They are functions in themselves, with ease of reuse overall.
  Yeah they are relatively useful, and the points that are made global within
  them, stay global within them, but accessible to any function that is not in
  the namespace itself.
*/
namespace display {
  // Variables active within the namespace.
  int width;
  int height; 
  bool visible;

  void foo() { // Function foo of the given namespace.
    width = 33; // The variable width has been instantiated already.
    std::cout << width << std::endl;  // No need for the display tag in here.
  }
}

int main() {
  display::foo(); // foo is a function within the namespace, outline it.

  std::cout << display::width << std::endl; // Can't get to it without the tag
  
  display::width = 50; // With the tag the same variable can be altered. 
  std::cout << display::width << std::endl;
  /*
    Will not work, due to the fact that outside the namespace.
    width does not exist. The program main does not know how to access it.
    The tag that is added above yields the accessing capabilities.
 
    //The below statement, yields a simple compilation error.
    height = 33;
  */
}

