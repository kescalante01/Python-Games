#Calculator

x=int(input('Enter x:' ))
y=int(input('Enter y:' ))

operator = input('Do you want to add (+) ,subtract(-),mult (*), divide (/)?: ')

multiply = lambda x,y: x* y

divide= lambda x,y: x/y

addition= lambda x, y: x +y


subtract= lambda x, y:  x-y


#now that the functions have been defined. This is the operational logic of the program.

if operator =='add':
    print('Addition of x and y: ', addition(x, y))
elif operator =='subtract':
    print('Subtraction of x and y: ', subtract(x, y))
elif operator =='mult':
    print('Multiply of x and y: ', multiply(x, y))
elif operator =='divide':
    print('Divide of x and y: ', divide(x, y))
else:
    print('Operator invalid. Try again with the correct options')


