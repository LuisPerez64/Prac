/*
 * permanence --
 *  Illustrates the value, and use of the static keyword, and how it alters
 *   the scope manipulation of the program.
 *
 * Author: Steve Oualline / Comments By Self.
 * 
 * Usage: N/A, no interaction.
 *
 * Purpose: Demonstate the use of the keyword static, and how it affects 
 *  scope control within the program, and how to use that, in a small fashion,
 *  to keep things moving as they should within the function.
 */
#include <iostream>

int main() {
  // Loop just to exhibit scope and locality of permanent, and temporary vars.
  for(int loopCounter(0); loopCounter < 3; ++loopCounter) {
    int temporary(1); // Initialized evey loop around.
    static int permanent(1); // Initialized once, and holds until program exits
    
    std::cout << "Temporary: " << temporary << " Permanent: " << permanent
	      << std::endl;
    ++temporary; 
    ++permanent;
  }
  
  /*
    Output:
    Temporary: 1 Permanent: 1
    Temporary: 1 Permanent: 2
    Temporary: 1 Permanent: 3
  */

  /*
    std::cout << "Permanent outside function scope: " << permanent;
    This fails, because even though permanent is declared, it is 'global'
    within the scope that calls it. It will not be able to be used without 
    being in the scope of that function, if within a function, and the function
    is called the variable still holds that same value, from when the function
    ended. This is really good for the use within a counter setting, within a 
    function.
  */

  return(0);
}
