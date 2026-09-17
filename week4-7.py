v,h,m,r,p,t = 8200.0, 140.0, 950.0,6370.0,0.06,18.0

x =v**3/(r*(h+t)*(p+0.04)*(1+h/r)**2)+ m**2*t / ((r-h)*(p+0.1))
print("My ID ends with 7")
print("Result =",round(x,5))