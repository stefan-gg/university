import py_expression_eval
from math import sin
from Equation import Expression
from sympy import symbols
from sympy import sympify, solve, Eq

from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')
print(solve(x**2 - 1, x))

x, y = symbols("x y")
#expr = sympify('2**2 / 3 + 5 + x + y', evaluate=False)
#expr.subs(x, 2)
#print(expr.subs(x, 2))

try:
    expr = Eq(sympify("x+y", evaluate=False), sympify("4", evaluate=False))
    expr2 = Eq(sympify("x-y", evaluate=False), sympify("0", evaluate=False))
    expr3 = Eq(sympify("x-2*y", evaluate=False), sympify("-22", evaluate=False))
    solution = solve((expr, expr2, expr3),(x, y))
    print(solution[x])
    print(solution[y])
#print(solve(expr, x))
except:
    print("No solution found for the equations.")


# formula = "sin(x)*x**2"
# code = parser.expr(formula).compile()
# x = 10
# print(eval(code))

# parser = py_expression_eval.Parser()

# exp = parser.parse('x+v+a=1')

# print(exp.variables())

# print(parser.evaluate('x + v * x + a + 3 * x^2 / 2', {"x":2, "v":1, "a":1}))
# fn = Expression("2x+y+2", ["x","y"])
# fn(0,40)

# print(fn)