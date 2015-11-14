#include<stdio.h>

int array[] = {23,34,12,17,204,99,16};
#define TOTAL_ELEMENTS (sizeof(array) / sizeof(array[0]))

/*
  Whats wrong. The Total Elements point returns an unsigned long int, and with 
  it's comparison to a negative number the negative number yields the maximum
  value that is able t0 be held in an ULI. The condition is negated from the 
  beginning.
int main()
{
  int d;
  for(d= (-1);d <= (TOTAL_ELEMENTS-2);d++)
    printf("%d\n",array[d+1]);

  return 0;
}
*/


int main()
{
  int d;
  //  The fix, cast total elements as a signed int
  for(d= (-1);d <= (signed)(TOTAL_ELEMENTS-2);d++)
    printf("%d\n",array[d+1]);

  return 0;
}
