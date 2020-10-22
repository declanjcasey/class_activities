#include <stdio.h>
#include <string.h>

struct student
{
  int id;
  char name[20];
  float percentage;
};

// TODO: create another structure variable

int main()
{
  struct student record = {0}; //Initializing to null

  record.id = 1;
  strcpy(record.name, "Janyl");
  record.percentage = 96.5;

  printf(" Id is: %d \n", record.id);
  printf(" Name is: %s \n", record.name);
  printf(" Percentage is: %f \n", record.percentage);

  // TODO: test the newly created struct

  return 0;
}
