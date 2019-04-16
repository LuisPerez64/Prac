#include <iostream>

int euclidean(int, int);

int main() {
  int inp1, inp2;

  std::cin >> inp1 >> inp2;
  std::cout << euclidean(inp1, inp2) << std::endl;

  return(0);
}


int euclidean(int inp1, int inp2) {
  if(inp1 < inp2) {
    int temp = inp1;
    inp1 = inp2;
    inp2 = temp;
  }

  int retVal(1), retCheck(0);

  while(inp2 != 0) {
    retCheck = inp1 % inp2;
    if(retCheck== 0) {
      retVal = inp2;
      break;
    } else {
      inp1 = inp2;
      inp2 = retCheck;
    }
  }

  return(retVal);
}
