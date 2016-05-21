#	brent's quick'n'dirty voltage divider python script
vs = float(input("Voltage Source (V)= "))
r1 = float(input("Resistor 1 (ohms)= "))
r2 = float(input("Resistor 2 (ohms)= "))
vout = (vs*r2)/(r1+r2)
print("{} {} V".format("VOUT=", vout))
