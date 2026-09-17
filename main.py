v,h,m,r,p,t = 8200.0, 140.0, 950.0,6370.0,0.06,18.0

x =v**2.5 / ((h+10)*(t+5)) *(m/(r+h))**0.5 + (p*v / ((p+0.02)*t))
print("My ID ends with 1")
print(f"Result = {x:.5f}")