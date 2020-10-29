/**
 * Janyl Jumadinova
 * Demonstration of arrays (two kinds) in C++
 * This simply shows how to declare ordinary (C-like) arrays as well
 * as "array containers" (C++ 2011), how to index elements, how to
 * compute sizes (NOTE: sizes are fixed at compile time!), how to
 * iterate over arrays.
 *
 * To compile and run using the standard "a.out" name for the executable:
 *     g++  -std=gnu++11  array1.cpp
 *     ./a.out
 *
 * (Or, if you prefer to give a different name to the executable:)
 *     g++  -std=gnu++11  array1.cpp  -o  someothername
 *     ./someothername
 */

#include <iostream>
#include <array>
#include <string>

using namespace std;

int main() {
  // First, "ordinary" arrays (similar to Java, C, many other languages):
  int array1[] = {10, 20, 30, 40, 50, 60, 70};
  double array2[] = {2.14159, 1.71828, 0.414, 0.732};
  string array3[] = {"hello", "hi", "howdy", "g'day", "goodbye", "bye", "ta"};

  cout << "size of array array1 (in bytes): " << sizeof array1 << endl;
  cout << "size of array array2 (in bytes): " << sizeof array2 << endl;
  cout << "size of array array3 (in bytes): " << sizeof array3 << endl;

  // Use "[]" to index ordinary arrays:
  for (int j = 0; j < 4; j++) {
    array1[j]++;
  }

  cout << "Contents of arrays array1, array2, and array3:" << endl;
  for (int element : array1) {
    cout << element << " ";
  }
  cout << endl;
  for (double element : array2) {
    cout << element << " ";
  }
  cout << endl;
  for (string element : array3) {
    cout << element << " ";
  }
  cout << endl;

  // Next, the "array" library (added to C++ in 2011)
  array<int,7> array4 = {-10, -20, -30, -40, -50, -60, -70};
  array<double,4> array5 = {-4.14159, -3.71828, -2.414, -2.732};
  array<string,7> array6 = {"olleh","ih","ydwoh","yad'g","eybdoog","eyb","at"};

  cout << "size of array array4: " << array4.size() << endl;
  cout << "size of array array5: " << array5.size() << endl;
  cout << "size of array array6: " << array6.size() << endl;

  // Use "[]" to index elements of the  array class:
  for (int j = 0; j < 4; j++) {
    array5[j]++;
  }

  cout << "Contents of arrays array4, array5, and array6:" << endl;
  for (int element : array4) {
    cout << element << " ";
  }
  cout << endl;
  for (double element : array5) {
    cout << element << " ";
  }
  cout << endl;
  for (string j : array6) {
    cout << j << " ";
  }
  cout << endl;
}