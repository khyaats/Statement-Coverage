Overview

In  particular,  you  will  need  to  track  and  print  out  the  statement  coverage  information  for  each 
pair of (a program, its associated input). 

Input: 
A single-function program written in Python and its associated input. They can be read from files, specified as strings in configuration files, etc., depending on your implementation. 

Output: 
Printing out the statement coverage by  prefixing each  statement with either 
  1.  a hashtag (the # symbol) if the statement is never exercised or 
  2.  spaces if the statement is exercised. 
The expected output format  for each statement is <hashtag_or_spaces>  <line_number> <statement>, where the line number starts from 1. We provide examples of the expected output below.

Loop Handling: 
If the program has (infinite) loops or recursions, please set the maximum execution time as 2 minutes for simplicity purposes, and then collect the covered or uncovered statements. 

