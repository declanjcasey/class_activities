import java.util.Arrays;

public class Array {
  public static void main(String[] args) {
    int array1[][] = new int[3][4];  // 3 by 4 array
    int array2[][] = new int[3][];   // 3 by ?? array

    array2[0] = new int[10];
    array2[1] = new int[5];
    array2[2] = new int[4];

    Arrays.fill(array1[0],10);
    Arrays.fill(array1[1],20);
    Arrays.fill(array1[2],30);

    Arrays.fill(array2[0],40);
    Arrays.fill(array2[1],50);
    Arrays.fill(array2[2],60);

    print("array1 = ", array1);
    print("array2 = ", array2);
  }

  public static void print(String str, int[][] array) {
    System.out.println(str);
    for (int[] row : array) {
      for (int i : row) {
        System.out.print(i + " ");
      }
      System.out.println();
    }
  }
}