# CMPSC 201: Class Activity 4

## Scope Rules in Javascript

Of course, it is not possible to explain JavaScript in any reasonable amount of detail in just a few paragraphs, but we note a few facts about it:

- Although it is not the same as Java, it shares much common syntax:

  - Statements end with a semicolon ";".

  - Most of the usual arithmetic, comparison, and boolean operators are used, as well as the boolean constants true and false (- * / % && || ! == < <= > >= !=).

  - However, the "/" operator will not do integer division, i.e., "25/10" is 2.5 in JavaScript (in Java it would be 2).

  - Strings can be enclosed either within single quotes or double quotes; the "+" operator is concatenation, just as in Java (so `"hello "+'world'+35` is the same as `"hello world35"`.

  - The syntax of "if" "if...else", "for", and "while" loops is the same in Java and JavaScript.

- However, there are many differences as well:

  - There are no type declarations; a variable's type can change at run time (we say JavaScript is dynamically typed).

  - As a result, to declare a variable we use the word "var", e.g., `var a = 20, b = true, c = "hello";`

    - Additionally, variables do not even have to be declared (except in "strict mode", which we will consider later); if it doesn't appear in a var statement, a variable is considered to be declared the first time it is used.

  - Because JavaScript is used for scripting Web pages, most output consists of generated HTML; consequently, we will use a debugging environment called the JavaScript console to see program output.

## An Online JavaScript Test Environment

Go to the site [JSFiddle](http://jsfiddle.net). Click on the JavaScript link on the bottom left window and make sure that the menus say "No-Library (pure JS)" and "onLoad". In your Browser menu, open the "JavaScript console" (it may be under "Tools/Developer Tools" or "View/Developer" or some other menu/submenu heading; it may simply be named "Console" or "Browser Console"). For example, in Firefox you can click on "Tools/Web Developer/Browser Console".

For you class activity 4 you are invited to complete specific steps outlined in the `activity4.md` file and answer questions specified after each step of the activity.

### Submission

Commit the modified `activity4.md` file to your class activities repository.
