/* Janyl Jumadinova
* Demonstration of closures in C#
* mcs Closure.cs -out:closure
* ./closure
*/

using System;

class Closure {
  static void Main(string[] args) {
    Func <int,int> g = returnFunc(7);
    Func <int,int> h = returnFunc(100);

    // Note that, despite that fact that "returnFunc" has finished
    // executing, g and h still "remember" the values of x and y
    // that were active when returnFunc was called.
    // This is due to closure.
    Console.WriteLine(g(9));
    Console.WriteLine(h(300));
  }

  // returnFunc returns an int-valued function of one int:
  static Func<int,int> returnFunc(int x) {
    int y = 10; 
    // Note that both x and y are LOCAL variables, 
    // declared in returnFunc
    Func <int,int> g = delegate(int z) { return x+y+z; };
    return g;
  }
}
