#include <stdio.h>
int main()
{
   int* pointer;
   int var;

   var = 22;
   printf("Address of var: %p\n", &var);
   printf("Value of var: %d\n\n", var);  // 22

   pointer = &var;
   printf("Address of pointer: %p\n", pointer);
   printf("Content of pointer: %d\n\n", *pointer); // 22

   var = 11;
   printf("Address of pointer: %p\n", pointer);
   printf("Content of pointer: %d\n\n", *pointer); // 11

   *pointer = 2;
   printf("Address of var: %p\n", &var);
   printf("Value of var: %d\n\n", var); // 2

   return 0;
}
