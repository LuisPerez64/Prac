#include <iostream>
#include <vector>
#include <string>

void fillVector(std::vector<int> &series, int filler);
int traverseMatrix(std::vector<std::vector<int> > &matrix);
int getMaxStraight (std::vector<int> &vector);
int getMaxDown(std::vector<std::vector<int> > &matrix, int index);
int getMaxDiagonalRight(std::vector<std::vector<int> >&matrix,
		   int iIndex, int jIndex);
int getMaxDiagonalLeft(std::vector<std::vector<int> >&matrix,
		       int iIndex, int jIndex);  
int staticCount(20); // No need for this to be static as its already global

int main(int argc, char *argv[]) {
  std::vector<std::vector<int> > matrix;
 
  while (std::cin and staticCount) {
    std::vector<int> series;
    fillVector(series, 20);
    matrix.push_back(series);
  }
  int result(traverseMatrix(matrix));

  std::cout << "Result: " << result << std::endl;
  return 0;
}

void fillVector(std::vector<int> &series, int filler){
  int count(filler);
  int input(0);
 
  std::vector<int>::iterator it(series.begin());

  while (count and std::cin) {
    --count;
    std::cin >> input;
    if (staticCount)
      series.push_back(input);
  }
  --staticCount;

  return;
}

int traverseMatrix(std::vector<std::vector<int> > &matrix){
  int index(20);
  int product(0), newProduct(0);

  // Always less than One, due to the off by one error     
  while (index) { // Get the greatest straight line series
    product = getMaxStraight(matrix.at(index - 1));
    if (product > newProduct)
      newProduct = product;
    --index;
  }
  
  // Get the greatest amount going vertically
  for (int iIndex(0); iIndex <= (signed) matrix.size() - 1; ++iIndex){
    product = getMaxDown(matrix, iIndex);
    if (product > newProduct)
      newProduct = product;
  }
  
  for (int iIndex(0); iIndex < 17; ++iIndex) 
    for (int jIndex(0); jIndex < 17; ++jIndex) {
      product = getMaxDiagonalRight(matrix, iIndex, jIndex);
      if (product > newProduct)
	newProduct = product;
    }
    
  for (int iIndex(19); iIndex > 3; --iIndex) 
    for (int jIndex(0); jIndex < 17; ++jIndex) {
      product = getMaxDiagonalLeft(matrix, iIndex, jIndex);
      if (product > newProduct)
	newProduct = product;
    }
  
  return newProduct;
}

int getMaxStraight (std::vector<int> &vector) {
  int product(1);
  int newProduct(0);
  int count(0);
  int multIndex(0);

  std::vector<int>::iterator vectorIter(vector.begin());
  while (vectorIter != vector.end()) {
    while (count < 4) { // Hardwired for now
      if (vectorIter == vector.end())
	break;
      product *= *vectorIter;
      ++vectorIter;
      ++count;
    }

    if (product > newProduct)
      newProduct = product;
    // Move the index forward one step to get the new product of the series.
    count = 0;
    product = 1;
    ++multIndex;
    vectorIter = vector.begin() + multIndex;
  }

  return(newProduct);
}

int getMaxDown(std::vector<std::vector<int> > &matrix, int index) {
  int product(1), newProduct(0);
  int multIndex(0), count(0), externCount(0);
  //std::vector<std::vector<int> >::iterator matrixIt((matrix.begin()+index)); 
  
  while (multIndex < 17) {
    while (count < 4) {
      ++count;
      product *= matrix.at(externCount).at(index);
      ++externCount;
    } externCount -=3;
    if (product > newProduct)
      newProduct = product;
    // Move the index forward one step to get the new product of the series.
    count = 0;
    product = 1;
    ++multIndex;
  }

  return newProduct;
}

int getMaxDiagonalRight(std::vector<std::vector<int> >&matrix,
		   int iIndex, int jIndex) {  
  int count(0), product(1);
  while (count < 4) {
    product *= matrix.at(iIndex).at(jIndex);
    ++iIndex; 
    ++jIndex;
    ++count;
  }
 
  return product;
}

int getMaxDiagonalLeft(std::vector<std::vector<int> >&matrix,
		   int iIndex, int jIndex) {  
  int count(0), product(1);
  while (count < 4) {
    product *= matrix.at(iIndex).at(jIndex);
    --iIndex; 
    ++jIndex;
    ++count;
  }
 
  return product;
}
