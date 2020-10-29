C Janyl Jumadinova
C  Demonstration of column-major order in Fortran (specifically, Fortran 95)
C
C To compile and run using the standard "a.out" executable name:
C     f95 array2.for
C     ./a.out
C
C To use some other name for the executable file:
C     f95 array2.for -o someothername
C     ./someothername
C
C Just for fun, I've included some other things in this program that
C illustrate things like the "implicit" statement, an example of an
C "implied do-loop" (in the first "write" statement), and (throughout)
C a demonstration of the fact that Fortran is a "CASE INSENSITIVE"
C language. I have also adopted a number of old-fashioned Fortran
C usages that have been superseded by more "modern" constructs.

C Create a 4-by-2 array and a linear array of size 8, then "union" them
C (i.e., make them share the same memory). ("Equivalence" is like the
C "union" structure in C)

      IMPlIciT iNteGER (a-z)
      integer,dIMenSiOn(4,2) :: array1
      INtegEr,dimension(8) :: Array2
      eQUiVaLENce (Array1,array2)

C Fill and print the linear array:
      do 10 j = 1,8
10      array2(j) = 10*j

      print *,"Elements of array2:"
      write(*,'(8i3)')(array2(j),j=1,8)

C Now print the elements of the two-dimensional array that shares space:
      PrinT *,"Elements of array1 by rows:"

      dO 30 j = 1,4
        do 20 k = 1,2
20        WriTe(*,'(i3)',advance='no'),array1(j,k)
30      print *
      stop
      end