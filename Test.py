str_length = input("Please type Length: \n")
str_width = input("Please type Width: \n")
str_price = input("How much for 1 meter? : \n")

#conver type --> float
length = float(str_length)
width  = float(str_width)
price  = float(str_price)

Area = length*width
total_price = price*Area

str_Area= str(Area)
str_total_price = str(total_price)
print("The total area is: "+ str_Area)
print("Give the guy: "+str_total_price + "$")