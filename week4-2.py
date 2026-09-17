v,h,m,r,p,t = 8200.0, 140.0, 950.0,6370.0,0.06,18.0
x = p**0.5 * v**3 / (2*r*(t+12)) * (1- h/r)**4 + (m*h / ((m-100)*p))
print("My ID ends with 2")
print("Result =",round(x,5))