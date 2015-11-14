#ifndef MY_TRIANGLE_HPP
#define MY_TRIANGLE_HPP

class Triangle {
 public:
  //Constructor / Destructor
  Triangle();
  ~Triangle();

  // Accessors / Mutators
  void printOutAllValues();
 private: 
  int knownCount; // The count of all the variables that are known so far.
  // Iterative function point ends when this equals the needed value.

  // The basic trig identities. SOH CAH TOA
  float sineTheta;      // Sine function           OPP/HYP
  float cosineTheta;    // Cosine function         ADJ/HYP
  float tangentTheta;   // Tangent function        OPP/ADJ
  float cotangentTheta; // Reciprocal of Tangent   1/Tangent
  float secantTheta;    // Reciprocal of cosine    1/Cosine
  float cosecantTheta;  // Reciprocal of sine      1/Sine 

  // Points of the triangle that are known/unknown.
  float HYP; // Length of Hypotenuse
  float ADJ; // Length of Adjacent
  float OPP; // Length of Opposite
  float angleTheta; // Angle theta in the triangle.
  // User implementation points
  // True if user is using degrees, else convert theta to degrees.  
  bool isInputInDegrees;

  //This is where it gets somewhat tedious;
  // Relay the parts of the triangle that are known or not
  bool isHYPKnown, isOPPKnown, isADJKnown; // The three sides of the triangle.
  bool isCosineKnown, isSineKnown, isTangentKnown; // Base trig Identities
  bool isSecantKnown, isCosecantKnown, isCotangentKnown; // Base inverse ^^
  bool isAngleThetaKnown; //angle Theta, the workhorse. 

  // Function that calculates everything based on initial input;
  void getUserKnownValues(); // User inputs what they know of the triangle
  void inputKnownValue(int usersChoice); //Place the input into the container
  void wasInputValueKnown(bool &inputBoolean); // Toggle for the knowns.
  void wrongInputValue(bool &inputBoolean, float &inputContainer);
  void calculateAllValuesInDegrees(); // The heart of it all.
  void calculateLengths(); // Calculate the lengths of the base Variables.
  void calculateTrigIdentities(); //Calculate the trigonometric Identities.
  // void countTheKnowns(); // Count the known variables in the triangle.
};

// Helper functions for the Class.
void printUserKnownValuesMenu();

#endif  //MY_TRIANGLE_HPP
