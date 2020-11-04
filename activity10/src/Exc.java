import java.util.Scanner;

/** 
* Exc.java -- demonstrate Exceptions.
*
* To compile and execute (with timing information):
*     javac Exc.java
*     time java Exc 
*/
public class Exc {
   public static void main(String[] args) //throws Exception
   {
      Scanner in = new Scanner(System.in);
      int num1 = in.nextInt();
      int num2 = in.nextInt();
      System.out.println(f(num1,num2));
   }

   public static int func(int num1, int num2) //throws Exception
   {
//      try {
        return num1/num2;
//      } catch(Exception e) {
//        System.out.println(e);
//        return 0;
//      }
   }
}
