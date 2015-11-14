#include "myTriangle.hpp"
#include <iostream>

Triangle::Triangle():
  knownCount(0), isHYPKnown(false), isOPPKnown(false), isADJKnown(false),
  isCosineKnown(false), isSineKnown(false), isTangentKnown(false),
  isSecantKnown(false), isCosecantKnown(false), isCotangentKnown(false),
  isAngleThetaKnown(false), isInputInDegrees(false),
  // Giving values that are impossible to attain                               
  sineTheta(NULL), cosineTheta(NULL), tangentTheta(NULL), secantTheta(NULL),
  cosecantTheta(NULL), cotangentTheta(NULL), HYP(NULL), OPP(NULL), ADJ(NULL) {
  
  getUserKnownValues();
  calculateAllValuesInDegrees();
}

Triangle::~Triangle() {
  std::cout << "It's gone now" << std::endl;
}
