#include <stdio.h>

int isPalindrome(char * input);

int main() {
  char * strArray[] = {"", "1", "11", "12", "111", "112"};
  for(int i = 0; i < 6; ++i)
    printf("%d \n", isPalindrome(strArray[i]));
}

int isPalindrome(char* input) {
  char *temp = input;
  
  while(*temp)
    ++temp;
  --temp;

  while(*input) {
    if (*input != *temp)
      return 0;
    ++input;
    --temp;
  }

  return 1;
}
