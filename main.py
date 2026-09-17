v = 8200.0
h = 140.0
m = 950.0
r = 6370.0
p = 0.06
t = 18.0
x =( v**2.2/ (r*(h+25)) )*( 1+p/0.1  )**1.5 + (m**2 / ((m+500)*t))
print("My ID ends with 0")
print(f"Result = {x:.5f}")