#!/usr/bin/python
#
# Voltage divider calculator
# Will find the missing value in a voltage divider setup
#

#Function definitions:
#Uses Extended ASCII Chars
def printcircuit (VoltSource, VoltOut, Res1, Res2):
    print("\n")
    print("          VIN = {0:6.2f} V".format(VoltSource))
    print("           ║")
    print("  ╔════════╩══════════╗")
    print("  ║ R1 = {0:8.2f} ohm ║".format(Res1))
    print("  ╚════════╦══════════╝")
    print("           ║")
    print("           ╠════ Vout = {0:6.2f} V".format(VoltOut))
    print("           ║")
    print("  ╔════════╩══════════╗")
    print("  ║ R2 = {0:8.2f} ohm ║".format(Res2))
    print("  ╚════════╦══════════╝")
    print("           ║")
    print("          GND")
    print("\n")

#Start
print("Enter the known values, skip if unknown(only 1)")

#Test each input
VI = input("Voltage Input (Vi):")
if VI:
    VI = float(VI)
else:
    print("No Vi given, using 5v as a base")
    VI = 5.0

VO = input("Voltage Output (Vo):")
if VO:
    VO = float(VO)
else:
    VO = False

R1 = input("Resistor 1 (ohms):")
if R1:
    R1 = float(R1)
else:
    R1 = False

R2 = input("Resistor 2 (ohms):")
if R2:
    R2 = float(R2)
else:
    R2 = False


if  (not VO) and R1 and R2:
    VO = VI * (R2/(R1+R2))
    printcircuit(VI, VO, R1, R2)
elif VO and (not R1) and R2:
    R1 = (VI/VO)*R2 - R2
    printcircuit(VI, VO, R1, R2)
elif VO and R1 and (not R2):
    R2 = R1/((VI/VO) - 1)
    printcircuit(VI, VO, R1, R2)
else:
    print("Too many unknowns")

