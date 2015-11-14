#include <iostream>

int testVar = 10; // testVar within a global scope.

namespace N {
  int testVar = 100; // Test var that belongs to namespace N 
  
  void foo() {
    int testVar = 1000; // Test var local to the function main.
    
    std::cout <<"Scope within the function foo: " << testVar 
	      <<std::endl; // This is the testVar that is local
    std::cout <<"Scope within the namespace N: " << N::testVar 
	      << std::endl; // Namespace's testVar
    std::cout << "Scope within the global scope: " << ::testVar 
	      << std::endl; // Gloabl namespaces testVar
  }
}

int main() {
  N::foo(); // Calls function foo within the namespace N

  return(0);
}
