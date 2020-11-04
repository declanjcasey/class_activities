# Janyl Jumadinova
# Demonstration of generators in Python
# 
# Functions "call" and "response" are examples of "generator functions."
# Instead of using a "return", they use a "yield", which effectively
# suspends the function until it is resumed later using a "next", at
# which point the function resumes where it left off. 
#
# Variables "calls" and "responses" are "generator variables" that hold
# the results of calling the generator functions.

# Returns the sequence [1,2], [3,4], [5,6], [7,8] (four repetitions)
# (See https://en.wikipedia.org/wiki/One,_Two,_Buckle_My_Shoe )

def call():
  nums = [1,2,3,4,5,6,7,8]
  i = 0
  for j in range(20):
    yield nums[i:i+2]
    i = (i+2)%8

# Returns rhyming reponses to values generated in "call" (four repetitions).
# (See https://en.wikipedia.org/wiki/One,_Two,_Buckle_My_Shoe )
def response():
  rhymes = ["buckle my shoe","open the door","pick up sticks","lay them straight"]
  i = 0
  for j in range(20):
    yield rhymes[i]
    i = (i+1)%4

calls = call()         # NOTE: function "call" is called ONLY ONCE
responses = response() # NOTE: function "response" is called ONLY ONCE

# Repeatedly get the next values generated from "call" and "response":
for i in range(20):
   print next(calls)
   print next(responses)

