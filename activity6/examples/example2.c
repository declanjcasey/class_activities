/*
 Author: Janyl Jumadinova

 Description: Program to demonstrate
 the use of if/else statements and loops.
*/

#include <stdio.h>
int main() {
  int numbers[10];
  for (int i = 0; i < 10; i++) {
    numbers[i] = i + 1;
  }

  int count = 0;
  // determine if a number is even or add
  while (count < 10) {
    if (numbers[count] % 2 == 0) {
      printf("The number %d is even.\n", numbers[count]);
    } else {
      printf("The number %d is odd.\n", numbers[count]);
    }
    count++;
  }
}
