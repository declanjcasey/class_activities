#include <stdio.h>
int main()
{
  int num = 5;
  printf("num: %d\n", num);

  // Notice the use of & before var
  printf("address of num: %p\n", &num);
  return 0;
}
