v,h,m,r,p,t = 8200.0, 140.0, 950.0,6370.0,0.06,18.0

x = v**2.6 / ((r+h)*(p+0.15))*(t/(t+10))**2.5 + m*(v-1000)/(r*t**2)
print("My ID ends with 4")
print("Result =",round(x,5))