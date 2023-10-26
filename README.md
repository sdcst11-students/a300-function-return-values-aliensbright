## SDSS Computing Studies Python Assignment
### Assignment #006 Functions (Total Marks 12)

Objectives:
* Explore Modular Code with Functions
* Identify Parameters
* Identify and use Return Values
* Comments are an important part of creating functions

We have looked at quite a lot of commands and structures this year.
In addition to all of the math and logical operators as well as
the code structures that control program flow, we have also looked
at commands that do a specific task.

Consider the following:

pow(x,y) : which finds out the exponent of x to the power of y
math.floor(x) : which takes the float value of x and rounds it down to an int
int(x) : which takes a float value of x and converts it to an integer

These are examples of functions.  They are mini programs that can be created
to do a specific tasks.  A function has a number of things in common:

There is a function name, that is used when you want to execute or "call"
the function.
Parameters are the things that are located inside the brackets.  
These are important inputs that are needed to run the function or
mini program.  The parameters are variables that can be used within
the function

Return values:
The purpose of a function is generate a specific value, or tuple or
list that is sent back by the function and can be used in an 
expression or assigned to a value.

Comments:
Every function should include a comment that describes what the function
does.

Open up example1.py to see how a basic function can be created.

### 3 Tasks, 4 Problems
Note: The autograder will be doing tests to compare
the return values of your program, and no output is actually graded
You should be using output to check to see if your program works.
The expected values can be found in the "assignment_test.py" file
as "assertions"

##### Task 1
Create a function called sum() that takes 2 inputs
The return value is the sum of the 2 numbers
(2 points) 

##### Task 2
Create a function called largest.
The input is a list.
Your function should convert the list to a tuple so that you can sort
it and find the largest.
The return value is the largest value in the list
(2 points)

##### Task 3
Create a function called perimeter()
The input is a list or tuple.
The return value is the sum of all the numbers in the list
added together
(2 points)

##### Task 4
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)

##### Problem 1
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)

##### Problem 2
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)

##### Problem 3
Create a function called factors()
Input parameter is a positive integer
Output is a sorted list containing all of the factors of that number.
Note: A Factor is a positive integer that can be evenly divided
into another number.
Example: The factors of 10 are 1, 2, 5, 10
(2 points)

##### Extension
Create a program to determine the solutions for a quadratic equation
in the format ax^2 + bx + c = 0
A key is the discriminant: b^2 - 4 * a * c
If the discriminant is negative, there are no solutions
If the discriminant is zero, there is only 1 solution
If the discriminant is positive, there are 2 solutions

If the discriminant is a perfect square, then the equation can
be factored

If the discriminant is non zero, the solutions are:
x = (-b + sqrt(b^2 - 4 * a * c)) / 2a
x = (-b - sqrt(b^2 - 4 * a * c)) / 2a

Assignment criteria:
Create a program that inputs 3 float values: a, b, c
function numSolutions(a,b,c) returns an integer with the number of solutions
function solutions(a,b,c) returns a tuple with the solutions (note that if 1 solution,
then both solutions will be the same)

If there are no solutions:
output is: "There are no real solutions"

If there is one solution:
output is "There is 1 solution, x=??"

If there are two solutions:
output is: "The solutions are x=?? and x=??"
