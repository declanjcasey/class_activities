# CMPSC 201 Activity 6

## C Basics

If you never programmed in C, or you have but you have forgotten what it’s like, here are some quick pointers (no pun intended for those of you who know C!). This is intended only to help you with the in-class exercise from today - obviously the “rules” below do not hold for C programs in general!

- Comments are of the form / ∗ ... ∗ /. (Some C compilers allow the “one-line comment” format //..., but some do not. Ours does.)

- If you want to do any output (let's forget input for today!), put this line at the top: #include <stdio.h>

- Variables must be declared at the beginning (again, some C compilers allow you to insert declarations in the middle of a program, some don’t). In particular, our compiler allows us to write "for (int i = ...)"; some C compilers require you to declare `i` above the loop.

- To print an integer variable, say `x`, with an optional label in front, use: `printf(‘‘Optional label %d\n",x);`

- To print a string, just use:
`printf(‘"The string you want printed\n’");`

- The general form of the program is: 
```
#include <stdio.h>
int main() {
... statements ...
}
```

Here is a simple, but nasty C program (nasty because it uses "goto"):

```
/* Demonstrates goto */ 
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
```

## C and `goto` Activity

Working with a partner, write a C program (in `prog1.c`) using only int variables, `if` statements (but NOT else!), loops, `printf` statements, and (most importantly) `goto` statements. Then, rewrite your program (in `prog2.c`) without `goto` statements.

Use the example above for the use of `goto` statements (also, in `example1.c`) and a sample program in `example2.c` for use of `if/else` statements and loops. 

Keep the code simple, but try to come up with an example of ["spaghetti code"](https://en.wikipedia.org/wiki/Spaghetti_code) that (a) works correctly and (b) does something recognizable (such as sum the numbers from 1 to 10 or calculate a Fibonacci number or find a factorial).

In header comments, identify the programmers, and state the purpose of the programs.

- To compile a C program named "myprog.c" in the lab, type:

`gcc myprog.c -o myprog`

(but please don’t type `-o myprog.c` because this will erase your C program!).

- To execute it, type: ./myprog

## Submission

Before our next class session, please submit `prog1.c` and `prog2.c` to your class_activities repository. Each person is to
commit programs developed as a team to their own repository, however the programs within each team are expected to be identical.
      