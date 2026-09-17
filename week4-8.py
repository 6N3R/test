v,h,m,r,p,t = 8200.0, 140.0, 950.0,6370.0,0.06,18.0

x =t**1.5 *v**2.2 / ((h+40)*(m-200))*(1+ p*r/v)**3 + r*p/((h+t)*2)
print("My ID ends with 8")
print("Result =",round(x,5))