# CMPSC 201 Activity 10 - Haskell Activity

## Why Haskell?

To learn more about Haskell's relevance, you can read the first few paragraphs (if you don't have time to read the whole thing) of [Haskell, the Language Most Likely to Change the Way you Think About Programming](http://goo.gl/moQQzO). This does not necessarily represent my opinion (I don't really have enough experience with Haskell to have an opinion).

\noindent If you want a little more detail try reading [Why Haskell Matters](https://wiki.haskell.org/Why_Haskell_matters).

## Where Do I Start?

Go to the online tutorial [Learn You a Haskell for Great Good!](http://learnyouahaskell.com/) and just start with Section 2\. Starting Out. Try some of the examples in the "Ready, set, go!" and "Baby's first functions". You can skip examples that you don't think you need.

Here are a few things you might miss if you are not reading carefully:

- Some of the examples in the tutorial have a `ghci` prompt; others don't. The ones that don't were intended to be entered into a file and then loaded using the `:l` command.

- When typing negative numbers like -3 it is always a good idea to put parentheses around them: `(-3)`.

- If you type `x = 10` into the `ghci` environment it won't work (you have to type `let x = 10`). But in a Haskell file the word `let` is not needed.

- The files that you upload with the `:l` command are not scripts in the usual sense of the word -- they do not contain commands to be executed. Instead, they contain definitions of names and functions. You must still enter commands in the `ghci` environment to make use of these functions and definitions.

- Function arguments don't require parentheses. Thus, `sqrt 10` means "call `sqrt` with argument 10" and "take 3 [1,2,3,4,5]" takes the first three elements of the list [1,2,3,4,5]. But watch out, if you want `sqrt(sqrt(10))` then you must write `sqrt (sqrt 10)`; you'll get an error with `sqrt sqrt 10`.

- You can convert a two-operand function into an infix operator using back-quotes: `take 3 [1,2,3,4,5]` is the same as `3 'take' [1,2,3,4,5]`

- Comments in Haskell begin with two hyphens `--` and extend to the end of the line, like this: `-- Janyl Jumadinova -- Haskell function definitions`

We have `ghci` on the `progator`.

## Task

Create one Haskell function. Feel free to be whimsical and to have fun. This function does not have to have "real-world" applications.) Indicate in your comments how the function is to be used and provide examples of its usage. I understand the temptation to look up a Haskell function on the Web and use that; please feel free to experiment with such functions, but in the end produce something that is original to you. Save your function in a `src/example.hs` file and comment it.
