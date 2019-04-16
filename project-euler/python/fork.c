#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
int main() {
  pid_t childPid;

  childPid = fork();
  switch(childPid) {
  case 0:
    switch(fork()) {
    case 0:
      execlp("python", "python", "summationOfPrimes.py", NULL); 
      break;
    case -1:
      printf("Failed in second fork process.\n\n");
    default:
      wait(NULL);
      printf("\n\n\n\n\nWell this works huh\n\n\n\n\n");
      break;
    }
    break;
  case -1:
    printf("Failed on fork\n");
    break;
  default:
    wait(NULL);
    printf("Now I'm out of it\n");
    break;
  }
  
  return 0;
}
