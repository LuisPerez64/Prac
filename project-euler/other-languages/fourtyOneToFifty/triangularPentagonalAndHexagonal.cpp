#include <iostream>
#include <algorithm>
#include <vector>

int triangular(int input);
int pentagonal(int input);
int hexagonal(int input);

int main(int argc, char* argv[]) {
  std::vector<int> triangles, pentagon, hexagon, allThree;

  for (int index(1); index <= 1000000; ++index) {
    triangles.push_back(triangular(index));
    pentagon.push_back(pentagonal(index));
    hexagon.push_back(hexagonal(index));
  }
  
  for (int index(0); index < 1000000; ++index) {  
    if ((std::find(pentagon.begin(), pentagon.end(), triangles.at(index)) !=
	 pentagon.end())
	and 
	(std::find(hexagon.begin(), hexagon.end(), triangles.at(index)) !=
	 hexagon.end()))
      std::cout << index<< " ";
  }  
}

int triangular(int input) {
  return input * (input + 1) / 2;
}

int pentagonal(int input) {
  return input * (3 * input - 1) / 2;
}

int hexagonal(int input) {
  return input * (2 * input -1);
}
