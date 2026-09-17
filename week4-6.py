v,h,m,r,p,t = 8200.0, 140.0, 950.0,6370.0,0.06,18.0

x = m**1.5*v/ ((h+50)*(t+2))*((r-h)/ (r+h))**2 + v**1.8/ (r*(p+0.05))
print("My ID ends with 6")
print("Result =",round(x,5))