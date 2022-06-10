import py_expression_eval
from math import sin
from Equation import Expression

# formula = "sin(x)*x**2"
# code = parser.expr(formula).compile()
# x = 10
# print(eval(code))

parser = py_expression_eval.Parser()

exp = parser.parse('x+v+a=1')

print(exp.variables())

print(parser.evaluate('x + v * x + a + 3 * x^2 / 2', {"x":2, "v":1, "a":1}))
# fn = Expression("2x+y+2", ["x","y"])
# fn(0,40)

# print(fn)