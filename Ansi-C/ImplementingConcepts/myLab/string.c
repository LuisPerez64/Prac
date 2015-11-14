#include <stdio.h>

int strLen(char* input) {
  int i = 0;
  for(;*input; ++i, ++input);

  return i;
} 

int strCompare(char* input, char* input2) {
  int result = 1;
  if(strLen(input) == strLen(input2))
    while(*input2) {
      if(*input != *input2) {
	result = 0;
	break;
      }
      ++input;
      ++input2;
    }
  else 
    result =2;

  return result;
}
    
