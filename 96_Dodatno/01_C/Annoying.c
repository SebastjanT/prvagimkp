#include <stdio.h>

#define MAX_INPUT 100

int main(int argc, char *argv[]){
  // Infinate loop that repeats the users input back to them, if there is any (with many errors waiting to happen)
  char userInput[MAX_INPUT];

  while ((fgets(userInput, MAX_INPUT, stdin) != NULL) && (userInput[0] != '\n')){
    printf("%s", userInput);
  }

  return 0;
}