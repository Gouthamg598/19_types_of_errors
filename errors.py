'''name error'''
# a=6
# print(b)

'''value error:too many values'''
# a,b=5,6,9
# print(a)

'''ValueError: not enough values'''
# a,b,c=6,9
# print(b)

'''TypeError: unsupported operand type(s) for +: 'int' and 'str'''
# print(6+'65')
# print(5+'ldhlkj')

'''ZeroDivisionError: division by zero'''
# print(5/0)

'''SyntaxError: expected ':' syntax means structure/rules of the python '''
# for x in range(1,4)
#     print(x)

'''actual program'''
# for x in range(1,4):
#     print(x,end=' ')#1 2 3 

'''IndentationError: expected an indented block after 'for' statement on line 28'''
# for x in range(1,4):
# print(x,end=' ')#1 2 3 

'''to know the errors builtin errors in python'''
# print(dir(__builtins__))