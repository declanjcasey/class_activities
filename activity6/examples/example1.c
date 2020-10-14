/*
 Author: Janyl Jumadinova

 Description: Program to demonstrate
 the use of goto statements.
*/

#include <stdio.h>
int main() {
int i = 10;
      if (i > 5) goto THERE;
  HERE:
      printf("Now I'm here\n");
      goto FINISH;
  THERE:
      printf("Now I'm there\n");
      goto HERE;
  FINISH:
      printf("I'm done!\n");
}
