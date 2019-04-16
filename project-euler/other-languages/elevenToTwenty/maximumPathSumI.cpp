#include <iostream>
#include <vector>

void fillTheMatrix(std::vector<std::vector<int> > &matrix);
void traverseTheMatrix(std::vector<std::vector<int> > &matrix);

int main(int argc, char* argv[]) {
  std::vector<std::vector<int> > matrix;

  fillTheMatrix(matrix);
  traverseTheMatrix(matrix);
}

void fillTheMatrix(std::vector<std::vector<int> > &matrix) {
  int input(0), counter(0);

  while (true) {  // I like while trues, external conditionals...
    if (!std::cin) // Can just do while std::cin 
      break;
    std::vector<int> vect; // Iterator below.
  
    for (int index(0); index <= counter; ++index) {
      std::cin >> input;
      vect.push_back(input);
    }

    for (std::vector<int>::iterator it(vect.begin());
	 it != vect.end();
	 ++it)
      std::cout <<  *it << " ";
    std::cout << std::endl;

    ++counter;
    matrix.push_back(vect);
  }

}

void traverseTheMatrix(std::vector<std::vector<int> > &matrix) {

}
