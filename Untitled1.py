#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Code to find the root of a Cubic Equation
A = float(input("Enter the Value of A in the Cubic Equation: "))

B = float(input("Enter the Value of B in the Cubic Equation: "))

C = float(input("Enter the value of C in the Cubic Equation: "))

D = float(input("Enter the Value of D in the Cubic Equation: "))

Dis = (B * 2) * (C * 2) - (4.0 * A)*(C * * 3) - 4.0 * (B * * 3) * D - (27) * (A * * 2) * (D * * 2) + (18 * A * B * C * D)
Print("The value of the Discriminant is",Dis)

if Dis == 0:
    print("Real and Same Roots")
    
if Dis > 0:
    print("Real and Different Roots")
    
if Dis < 0:
    print("Complex roots Exist")

