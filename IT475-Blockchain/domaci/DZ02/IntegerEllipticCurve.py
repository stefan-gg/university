import sys

if (len(sys.argv) < 3):
   print("Korišćenje: python IntegerEllipticCurve.py prvi_parametar drugi_parametar")
   exit()

aa = sys.argv[1]
bb = sys.argv[2]
a = int(aa)
b = int(bb)

r = 4*a**3 + 27*b**2
if (r == 0):
   print("Error: (a, b) = ("+aa+", "+bb+") and 4a^3 + 27b^2 == 0")
   exit()

print("Elliptic equation : y^2 = x^3 + ax + b with (a, b) = ("
   +aa+", "+bb+")")

x = 0
r = x**3 + a*x + b
while (r >= 0):
  x = x - 1
  r = x**3 + a*x + b
print("Starting with : x = "+str(x))

while ( r<0 ):
  x = x + 1
  r = x**3 + a*x + b
print("First candidate : x = "+str(x))

y = 0
while (x < 100000):
   r = x**3 + a*x + b
   l = y**2

   while (l < r):
      y = y + 1
      l = y**2

   if (l == r):
      print("Point on curve : (x, y) = ("+str(x)+", "+str(y)+")")

   x = x + 1

print("Ended with (x, y, r, l) = "
   +str(x)+", "+str(y)+", "+str(r)+", "+str(l)+")")
exit()