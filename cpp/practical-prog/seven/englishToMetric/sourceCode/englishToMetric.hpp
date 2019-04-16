#ifndef ENGLISH_TO_METRIC_HPP
#define ENGLISH_TO_METRIC_HPP

inline bool validityCheck(const char &input); // Validity of input check (y/n);

bool runConverter(void); // Main within main, this is the heart of it all.    
  
void inputOutput(void);// This program runs the input/output operations        

// This function runs through, and makes the users output proper english       
// Produces miles, kilo(grams/meters), and whatever other units are being used.
void outputStringAssigns(const int &conversionChoice,
                         std::string &inputConversionType,
                         std::string &outputConversionType); // Assigns names.
 
// This one does the actual conversion of the input.                           
float doConversion(const int &conversionChoice, const float &numberToConvert);

#endif // ENGLISH_TO_METRIC_HPP
