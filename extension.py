#!python3
"""
NOTE:
If you complete this extension, call your teacher over to have it assessed


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
"""

def numSolutions(a,b,c):
    descriminant = b**2 - 4 * a * c
    if descriminant>0:
        sols=2
    if descriminant==0:
        sols=1
    if descriminant<0:
        sols='no real'
    return sols

def solutions(a,b,c,d):
    if d==2:
        solution1 = (-b - (b**2 - 4 * a * c)**0.5) / (2 * a)
        solution2 = (-b + (b**2 - 4 * a * c)**0.5) / (2 * a)
        solution1 = round(solution1,2)
        solution2 = round(solution2,2)
        solsList = [solution1,solution2]
    elif d==1:
        solution1 = (-b) / (2*a)
        solution1 = round(solution1,2)
        solsList = [solution1]
    else:
        solsList=[]
    return solsList
name = 'QUADRATIC EQUATION CALCULATOR.'
instructions = '\nI will be finding the real solutions of a quadratic equation of the form of ax^2 + bx + c = 0, they will be rounded to 2 decimal places. You will need to\ninput the "a", "b", "c" values.\n'

def title(m,n):
    # inputs none
    # return str of All the title and instructions on one line
    nameInst = m+n
    return nameInst

def main():
    # Display Title and Instructions
    print(title(name,instructions))
    # Your code and function calls should go here
    x = float(input('Enter the value attached to x^2:'))
    y = float(input('Enter the value attached to x:'))
    z = float(input('Enter the constant value:'))
    sols = numSolutions(x,y,z)
    solsList = solutions(x,y,z,sols)
    print('There are', sols,'solutions!')
    if sols=='no real':
        pass
    else:
        print('\nThe solutions are',solsList,'\n')


main()