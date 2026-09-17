v,h,m,r,p,t = 8200.0, 140.0, 950.0,6370.0,0.06,18.0
x = m*v**2 / (r*(h+t))*(p/(p+0.25))**1.5 + v**1.5 /((r-h)*(p+0.01))
print("My ID ends with 3")
print("Result =",round(x,5))