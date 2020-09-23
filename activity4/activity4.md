# CMPSC 201: Class Activity 4

## Tasks

If you haven't done so already, go to the site [JSFiddle](http://jsfiddle.net). Click on the JavaScript link on the bottom left window and make sure that the menus say "No-Library (pure JS)" and "onLoad". In your Browser menu, open the "JavaScript console" (it may be under "Tools/Developer Tools" or "View/Developer" or some other menu/submenu heading; it may simply be named "Console" or "Browser Console"). For example, in Firefox you can click on "Tools/Web Developer/Browser Console".

### Step 1

On the jsfiddle page, in the Window labeled "JavaScript", type the following short program, then click the "Run" button at the top of the screen:

```
var glob = 'one'; // global variable

function test() {
    glob = glob + "two";
    var loc = 'three'; // local variable
    unknown = 'four';  // which is this?
}

console.log("Initially, glob = "+glob);
//console.log("  loc = "+loc);
//console.log("  unknown = "+unknown);
test();
console.log("After calling test, glob = "+glob);
//console.log("  loc = "+loc);
console.log("  unknown = "+unknown);
```

Now try uncommenting each of the commented-out calls (one by one) to `console.log` to see what happens. You should see errors.

#### Step 1 Questions

1. Why is `unknown` defined after test is called but not before?

2. Why is `loc` undefined both before and after test is called?

### Step 2

There is a concept in programming languages called "hole in scope". Try this code:

```
var glob = 'one';

function test1() {
    glob = glob + 'two';
}

function test2() {
    var glob = 'three';
}

test1();
test2();
console.log(glob);
```

#### Step 2 Question

Is function `test2` within the scope of the first variable `glob`?

### Step 3

Java does not allow variables to be re-declared; JavaScript does. Therefore, things like the following are legal in JavaScript; the second declaration overwrites the first:

```
function test3() {
  var x = 10;
  var x = 'hello';
  console.log("x = "+x);
}
test3();
```

#### Step 3 Question

What is the output?

### Step 4

The `var` declaration in JavaScript does not obey block-scope (unlike declarations within block in Java and C). Opening a new block with "{...}" does not create a new scope for `var` variables. In the following, the declaration of `x` inside the for-loop overwrites the first declaration of `x`:

```
function test4() {
  var x = 10;
  for (i = 0; i < 10; i++) {
    var x = 'hello';
  }
  console.log("x = " + x);
}
test4();
```

We say that JavaScript has function scope rather than block scope.

#### Step 4 Question

What is the output?

### Step 5

Run the following (try to guess the output before running it):

```
function test5() {
  var x = 10;
  for (var i = 0; i < 10; i++) {
    var x = 'hello';
  }
  console.log("x = " + x);
  console.log("i="+i);
}
test5();
console.log("i="+i);
```

#### Step 5 Question

What is the output?

### Step 6

A few years ago, a new type of declaration was added to JavaScript: the `let` declaration. This behaves like `var` except that, within a new block, it respects block scope. In order to use this (at least in jsfiddle), we must add a line at the top to enter `strict` mode:

```
"use strict";
function test6() {
  var x = 10;
  for (let i = 0; i < 10; i++) {
    let x = 'hello';
  }
  console.log("x = " + x);
  //console.log("i="+i);
}
test6();
//console.log("i="+i);
```

#### Step 6 Question

What is the output? Explain the differences between these types by providing concrete examples of what you observe from running code in steps 5 and 6.

### Submission

Commit and push the modified `activity4.md` file to your class activities repository.
