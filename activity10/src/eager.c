/**
 * Janyl Jumadinova
 * Demonstration of eager evaluation.
 *
 * To compile and execute:
 *    gcc eager.c
 *    time ./a.out
 *
 */

#include <stdio.h>
#include <stdlib.h>

int count = 0;

int slow(int n) {
  count = 1+slow(n-1);
  return count;
}

int f(int a, int b) {
  return a+1;
}

int main() {
  
  int x;
  x = f(10,slow(1000000));
  //printf("%d\n",x);
} 